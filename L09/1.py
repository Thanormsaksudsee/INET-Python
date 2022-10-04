from tkinter import CENTER
import pgzrun

width = 400
height = 300

def draw():
    screen.fill((100, 200, 150))
    screen.draw.text('Hello World', topleft=(350,250), fontsize=30)

pgzrun.go()