import turtle

turtle.speed(5)
turtle.bgcolor("black")

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

def heart():
    turtle.color("blue", "red")

    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(112.65)

    curve() #Left Curve

    turtle.left(120)

    curve() # Right curve

    turtle.forward(111.64)
    turtle.end_fill()
    turtle.hideturtle()


heart()
turtle.done()
