from settings import *

class Engine:
    def __init__(self, game):
        self.game = game

    def update(self): 
        pass

    def draw_2d(self): #for debug purposes
        pass

    def draw_3d(self):
        pass

    def draw(self):
        ray.begin_drawing()

        #we actually start to draw here
        ray.clear_background(ray.BLACK)
        self.draw_3d()
        self.draw_2d()

        #end of drawing
        ray.end_drawing()



