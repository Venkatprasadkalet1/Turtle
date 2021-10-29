import turtle
from random import randint 

turtle.bgcolor('black') 
turtle.speed(100) 

for x in range(100): 
  
   r = randint(0,255) 
   g = randint(0,255)  
   b = randint(0,255) 
  
   turtle.colormode(255)  
   turtle.pencolor(r,g,b) 
   turtle.forward(100 + x) 
   turtle.right(95)
   for i in range(6):
      turtle.forward(150+x)
      turtle.right(60) 

turtle.done()

  