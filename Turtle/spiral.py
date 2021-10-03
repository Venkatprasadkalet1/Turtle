import turtle
import time

t=turtle.Turtle()
turtle.bgcolor('black')

t.speed(0)
a=['violet','blue','green','yellow','orange','red']

for i in range(300):
    t.pencolor(a[i%6])
    t.forward(i)
    t.right(57)

time.sleep(10)
