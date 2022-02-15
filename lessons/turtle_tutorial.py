from turtle import Turtle, colormode, done 
bob: Turtle = Turtle()
bob.penup()
bob.color('red')
bob.goto(45, 60)
bob.pendown()
bob.speed(100)

side_length: int = 300 
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
done()
