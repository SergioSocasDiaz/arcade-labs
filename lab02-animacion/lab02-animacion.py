import arcade
from lab02draw import dibujar_sol
import math


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
        self.posicionx=0
    def on_draw(self):
        self.clear()
        arcade.draw_rect_filled(arcade.XYWH(400,100,800,200),(246, 252, 129))
        dibujar_sol((math.cos(self.posicionx)*700)+50,500)
        self.posicionx+=0.01

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
