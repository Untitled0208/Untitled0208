

from turtle import *
import colorsys

speed(0)
hideturtle()
bgcolor('black')
tracer(1)
width(2)
h = 0.001

for i in range(90):
    color(colorsys.hsv_to_rgb(h, 1, 1))
    forward(120)
    right(60)
    forward(100)
    circle(10)
    right(120)
    h += 0.002
    color(colorsys.hsv_to_rgb(h, 1, 1))
    forward(120)
    left(60)
    forward(100)
    circle(10)
    right(115)
    h += 0.002

done()
