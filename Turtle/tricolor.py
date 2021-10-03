import turtle
import time

t=turtle.Turtle()
t.color('orange')
t.speed(0)
t.penup()
t.goto(-150,0)
t.pendown()
for i in range(72):
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.right(5)
t.penup()
t.goto(50,0)
t.pendown()
t.color('blue')
for i in range(72):
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.right(5)
t.penup()
t.goto(250,0)
t.pendown()
t.color('green')
for i in range(72):
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.right(5)
time.sleep(10)