

from turtle import *
import colorsys
bgcolor("black")
width(3)
tracer(10)
h=0
for i in range(500):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.002
    color(c)
    goto(0, 0)
    right(60)
    forward(5)
    circle(i, 10)
    right(90)
    forward(10)
    circle(i, 10)
    right(80)
    forward(15)
    circle(i, 20)
    right(70)
    forward(20)
    circle(i, 20)
    right(60)
    hideturtle()

done()
