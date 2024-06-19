

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
    forward(50)
    left(30)
    forward(75)
    left(150)
    circle(10)
    forward(60)
    left(90)
    forward(0)
    left(90)
    h += 0.02
    color(colorsys.hsv_to_rgb(h, 1, 1))
    forward(50)
    right(30)
    forward(75)
    right(150)
    circle(10)
    forward(60)
    right(90)
    forward(0)
    left(100)
    h += 0.02

done()



