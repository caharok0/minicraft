from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        base.camLens.setFov(90)
        land = Mapmanager()
        x, y = land.load_map('maps/my_map.txt')
        self.hero = Hero((x // 2, y // 2, 1), land)
game = Game()
game.run()