import pickle

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
        self.block.setTag("at", str(position))
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
        
    def find_blocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))
    
    def is_empty(self, pos):
        if self.find_blocks(pos):
            return False
        else:
            return True
        
    def find_hightest_empty(self, pos):
        x, y, z = pos
        z = 1
        while not self.is_empty((x, y, z)):
            z += 1
        return (x, y, z)
    
    def build_block(self, pos):
        x, y, z = pos
        new = self.find_hightest_empty(pos)
        if new[2] <= z + 1:
            self.add_block(new)
            return new

    def destroy_block(self, pos):
        blocks = self.find_blocks(pos)
        for block in blocks:
            block.removeNode()
    
    def del_block_from(self, pos):
        x, y, z = self.find_hightest_empty(pos)
        pos = (x, y, z - 1)
        blocs = self.find_blocks(pos)
        for bloc in blocs:
            bloc.removeNode()

    def save_map(self):
        blocks = self.land.getChildren()
        with open("my_map.dat", "wb") as file:
            pickle.dump(len(blocks), file)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, file)

    def load_map_from_file(self):
        with open("my_map.dat", "rb") as file:
            length = pickle.load(file)
            for i in range(length):
                pos = pickle.load(file)
                self.add_block(pos)