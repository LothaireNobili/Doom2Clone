from source.settings import *
from source.engine import Engine

class Game:
    ray.init_window(WIN_WIDTH, WIN_HEIGHT, "Doom 2 clone")

    def __init__(self):
        self.dt = 0.0
        self.engine = Engine(game=self)

    def run(self):
        while not ray.window_should_close():
            self.dt = ray.get_frame_time()
            self.engine.update()
            self.engine.draw()
        
        ray.close_window()

if __name__ == "__main__":
    game = Game()
    game.run()