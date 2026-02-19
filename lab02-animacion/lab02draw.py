import arcade
def dibujar_sol(x,y):
    arcade.draw_circle_filled(x,500,50,(235, 247, 10))
    arcade.draw_rect_filled(arcade.XYWH(x,y,150,20),(235, 247, 10),0)
    arcade.draw_rect_filled(arcade.XYWH(x,y,150,20),(235, 247, 10),90)
    arcade.draw_rect_filled(arcade.XYWH(x,y,150,20),(235, 247, 10),45)
    arcade.draw_rect_filled(arcade.XYWH(x,y,150,20),(235, 247, 10),-45)
