class Mapmanager:
    def __init__(self):
        self.model = "models/block.egg"
        self.texture = "textures/block.png"
        self.colors = [
            (126, 132, 48, 1),
            (191, 83, 35, 1),
            (81, 206, 206, 1),
            (81, 74, 206, 1),
        ]
        self.add_land_node()

        
    def add_land_node(self):
        self.land = render.attachNewNode("land")
        
    def clear_land_node(self):
        self.land.removeNode()
        self.add_land_node()
        
    def set_color(self, z: int):
        if z <= 3:
            return self.colors[z]
        else:
            return self.colors[0]
    
        
    def add_block(self, position: tuple):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        color = self.set_color(position[2])
        self.block.setColor(color)
        self.block.setPos(position)
        self.block.reparentTo(self.land)
        
    def load_map(self, filename):
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line_lst = line.split(" ")
                for z in line_lst:
                    for z0 in range(int(z) + 1):
                        block = self.add_block((x, y, z0))
                    x += 1
                y += 1
            return x, y