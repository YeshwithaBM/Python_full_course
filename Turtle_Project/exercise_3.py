import turtle
import random
from turtle import Turtle

turtle.colormode(255)
tom = Turtle()
tom.width(15)
for _ in range(100):
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    directions=random.randrange(0,360,90)
    tom.setheading(directions)
    tom.pencolor((r,g,b))
    tom.forward(30)

    
tom.screen.mainloop()