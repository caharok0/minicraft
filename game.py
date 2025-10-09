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

        start_snd = self.loader.loadSfx("sounds/inecraft_forrest.ogg")
        start_snd.set_volume(0.2)
        start_snd.set_loop(True)
        start_snd.play()
game = Game()
game.run()