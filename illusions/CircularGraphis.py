import turtle
t = turtle.Turtle()

def square(l, a):
    for i in range(4):
        t.forward(l)
        t.right(a)

for i in range(200):
    square(100, 90)
    t.right(5)

t.done()
