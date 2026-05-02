import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 0
    b = randint(120, 255)

    Width = WIDTH
    Height = HEIGHT - 200

    for i in range(20):
        rect = Rect((0, 0), (Width, Height))
        screen.center = 150, 150
        screen.draw.filled_rect(rect, (r, g, b))

        r-= 10
        g+= 10

        Width -= 10
        Height += 10
        
pgzrun.go()
