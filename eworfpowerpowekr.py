improt pgzrun
from random import randint
WIDTH = 800
HEIGHT = 600

star = []
lines = []
start_time = 0
next_star = 0
total_time = 0

number_of_stars = 7

def create_stars():
    global start_time, star, lines, next_star

    lines = []
    star = []

    next_star = 0

    for i in range(number_of_stars):
        star = actor("star")
        star.pos = (randint(0, WIDTH), randint(0, HEIGHT))
        stars.append(star)