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
        self.add_block((1, 1, 1))
        
    def add_land_node(self):
        self.land = render.attachNewNode("land")
        
    def clear_land_node(self):
        self.land.removeNode()
        self.add_land_node()
    
        
    def add_block(self, position: tuple):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setColor(self.colors[0])
        self.block.setPos(position)
        self.block.reparentTo(self.land)