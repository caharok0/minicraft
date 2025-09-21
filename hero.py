class Hero:
    def __init__(self, position, land):
        self.swich_mode = None
        self.game_mode = True
        self.land = land
        self.hero = loader.loadModel("smiley")
        self.hero.setColor((100, 170, 245, 0))
        self.hero.setScale(0.3)
        self.hero.setPos(position)
        self.hero.reparentTo(render)
        
        self.camera_bind()
        self.accept_events()
        
    def camera_bind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.camera_mode = True
        
    def camera_up(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] -3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.camera_mode = False
        
    def swich_camera(self):
        if self.camera_mode:
            self.camera_up()
        else:
            self.camera_bind()
            
    def change_mode(self):
        if self.game_mode:
            self.game_mode = False
        else:
            self.game_mode = True
            
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
        
    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)
    
    def look_at(self, angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())
        
        dx, dy = self.check_dir(angle)
        
        return x + dx, y + dy, z
        
    def move_to(self, angle):
        """Обираємо як рухати гравця в залежності від режиму гри"""
        if self.game_mode:
            self.just_move(angle)
        else:
            self.try_move(angle)
    
    def just_move(self, angle):
        """рух гравця в режимі спостерігача"""
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    
    def try_move(self, angle):
        """рух гравця в ігровому рижимі"""
        pos = self.look_at(angle)
        if self.land.is_empty(pos):
            pos = self.land.find_hightest_empty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.is_empty(pos):
                self.hero.setPos(pos)
    
    def check_dir(self, angle):
       ''' повертає заокруглені зміни координат X, Y,
       відповідні переміщенню у бік кута angle.
       Координата Y зменшується, якщо персонаж дивиться на кут 0,
       та збільшується, якщо дивиться на кут 180.
       Координата X збільшується, якщо персонаж дивиться на кут 90,
       та зменшується, якщо дивиться на кут 270.
           кут 0 (від 0 до 20) -> Y - 1
           кут 45 (від 25 до 65) -> X + 1, Y - 1
           кут 90 (від 70 до 110) -> X + 1
           від 115 до 155 -> X + 1, Y + 1
           від 160 до 200 -> Y + 1
           від 205 до 245 -> X - 1, Y + 1
           від 250 до 290 -> X - 1
           від 290 до 335 -> X - 1, Y - 1
           від 340 -> Y - 1
       '''
       if 0 <= angle <= 20:
           return 0, -1
       elif angle <= 65:
           return 1, -1
       elif angle <= 110:
           return 1, 0
       elif angle <= 155:
           return 1, 1
       elif angle <= 200:
           return 0, 1
       elif angle <= 245:
           return -1, 1
       elif angle <= 290:
           return -1, 0
       elif angle <= 335:
           return -1, -1
       else:
           return 0, -1

    def accept_events(self, angle):
        x = (self.hero.getX())
        y = (self.hero.getY())
        z = (self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return x + dx, y + dy, z
    
    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)
        
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() - 90) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def up(self):
        if self.game_mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        if self.game_mode:
            self.hero.setZ(self.hero.getZ() - 1)
            
    def buld(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.game_mode:
            self.land.add_block(pos)
        else:
            self.land.buld_block(pos)
            
    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.game_mode:
            self.land.destroy_block(pos)
        else:
            self.land.del_block_from(pos)

    def accept_events(self):
        base.accept("c", self.swich_camera)
        base.accept("n", self.turn_left)
        base.accept("n" + "-repeat", self.turn_left)
        base.accept("m", self.turn_right)
        base.accept("m" + "-repeat", self.turn_right)
        base.accept("w", self.forward)
        base.accept("s", self.back)
        base.accept("a", self.left)
        base.accept("d", self.right)
        base.accept("q", self.down)
        base.accept("e", self.up)
        base.accept("z", self.change_mode)
        base.accept("v", self.buld)
        base.accept("b", self.destroy)

            