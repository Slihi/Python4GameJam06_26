import arcade
import random


#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255 , 0)
PURPLE = (255, 0, 255)
BROWN = (165, 42, 42)
TAN = (210, 180, 140)
GREY = (128, 128, 128)

# Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Platformer test"

# Window

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, SCREEN_TITLE, resizable=True)
        minimum_width = 1200
        minimum_height = 800
        self.set_minimum_size(minimum_width, minimum_height)

    def setup(self):
        pass

    def on_resize(self, width, height):
        pass

    def update(self, delta_time):
        pass

    def on_draw(self):
        # Kind of like window.clear()
        arcade.start_render()

        #Square_test
        square = arcade.create_rectangle_filled(400, 300, 50, 50, RED)
        
        
        #Draw   
        square.draw()
        pass


#Run 
if __name__ == "__main__":
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

