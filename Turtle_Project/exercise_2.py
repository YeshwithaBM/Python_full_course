# #My solution
# from turtle import Turtle, Screen

# s1=Screen()
# tom=Turtle()
# tom.shape("classic")
# tom.speed("fast")
# def move():
#     tom.penup()
#     tom.forward(100)
#     tom.pendown()
#     tom.pensize(4)

# move()
# tom.color("blue","black")
# for _ in range(2):
#     tom.right(120)
#     tom.forward(100)

# tom.right(120)
# move()
# tom.color("orange","black")
# for _ in range(3):
#     tom.right(90)
#     tom.forward(100)

# tom.right(90)
# move()
# tom.color("red","black")
# for _ in range(4):
#     tom.right(72)
#     tom.forward(100)

# tom.right(72)
# move()
# tom.color("orange","black")
# for _ in range(5):
#     tom.right(60)
#     tom.forward(100)

# tom.right(60)
# move()
# tom.color("pink","black")
# for _ in range(6):
#     tom.right(51.5)
#     tom.forward(100)
# tom.right(51.5)

# s1.mainloop()


### Optimized
import random
from turtle import Turtle

tom = Turtle()

colors = ["red", "green", "pink", "orange", "blue", "yellow" ,"purple"
           "brown", "burlywood", "chocolate1"]

def move(angle):
    tom.penup()
    tom.forward(100)
    tom.pendown()
    tom.pensize(4)
    tom.right(angle)

for i in range(3, 8):  # 3, 4, 5, 6, 7, 8
    angle = 360 / i
    tom.pencolor(random.choice(colors))
    move(angle)
    for _ in range(i-1):
        tom.forward(100)
        tom.right(angle)
    
tom.screen.mainloop()