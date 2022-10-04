
import pgzrun
from random import randint

WIDTH = 640
HEIGHT = 480


orange = Actor('human')


def draw():
    screen.clear()
    orange.draw()


def place_orange():
    orange.x = randint(10, 600)
    orange.y = randint(10, 400)


# function to get mouse event
def on_mouse_down(pos):
    if orange.collidepoint(pos):
        print('Good Shot!')
        place_orange()
    else:
        print('You missed!')


place_orange()
pgzrun.go()
