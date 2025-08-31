from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        base.camLens.setFov(90)
        land = Mapmanager()
        x, y = land.load_map('maps/my_map.txt')
game = Game()
game.run()