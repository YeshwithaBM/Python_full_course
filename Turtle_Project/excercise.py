from turtle import Turtle, Screen

s1=Screen()
tom=Turtle()
tom.shape("classic")

tom.speed("fast")
tom.penup()
tom.goto(-280,-0)
tom.pendown()
for _ in range(19):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()


s1.mainloop()