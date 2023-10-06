import turtle 
t=turtle.Turtle()
t.screen.bgcolor('black')
t.pensize(3)
t.color('brown')
t.left(90)
t.backward(100)
t.speed(400)
t.hideturtle()

def createTree(i):
    if(i<10):
        return
    else:
        t.forward(i)
        t.color('green')
        t.circle(2)
        t.color('brown')
        t.left(30)
        createTree(3*i/4)
        t.right(60)
        createTree(3*i/4)
        t.left(30)
        t.backward(i)

createTree(100)
turtle.done()