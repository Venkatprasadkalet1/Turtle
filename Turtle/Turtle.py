import turtle

t = turtle.Turtle()

t.speed(0)
turtle.bgcolor("black")


def curve(turtle_obj):
    for i in range(200):
        t.right(1)
        t.forward(1)

def draw_lines(turtle_obj):
    start_pos = t.pos()
    for i in range(260//20):
        t.right(20)
        t.forward(111.65)
        t.goto(start_pos)

t.color("blue", "red")

t.begin_fill()
t.left(140)
t.forward(111.65)
curve(t)

t.left(120)
curve(t)
t.forward(111.65)
t.end_fill()
t.hideturtle()
t.right(180)
draw_lines(t)


