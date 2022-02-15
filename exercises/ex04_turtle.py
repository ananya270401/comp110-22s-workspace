"""Exercise 4 Turtles."""

__author__ = '730466694'

from turtle import Turtle, colormode, done
from random import randint


def square(raphael: Turtle, x: float, y: float) -> None:
    """Draw a square."""
    raphael.penup()
    raphael.goto(x, y)
    colormode(100)
    raphael.pendown()
    i: int = 0
    while i < 4:
        raphael.forward(40)
        raphael.right(90)
        i = i + 1


def line(raphael: Turtle, x: float, y: float) -> None:
    """Draw a Triangle."""
    raphael.penup()
    raphael.color("white")
    raphael.goto(x, y)
    colormode(222)
    raphael.pendown()
    i: int = 0
    while i < 1:
        raphael.forward(75)
        raphael.left(45)
        i = i + 1


def circle(raphael: Turtle, x: float, y: float) -> None:
    """Draw a line."""
    raphael.color('yellow')
    raphael.begin_fill()
    raphael.penup()
    raphael.goto(x, y)
    raphael.pendown()
    i: int = 0
    while i < 1:
        raphael.circle(60)
        i = i + 1
    raphael.end_fill()


def rectangle(raphael: Turtle, x: float, y: float) -> None:
    """Draw a rectangle."""
    raphael.color('red')
    raphael.begin_fill()
    raphael.penup()
    raphael.goto(x, y)
    colormode(222)
    raphael.pendown()
    i: int = 0
    while i < 2:
        raphael.forward(250)
        raphael.left(90)
        raphael.forward(125)
        raphael.left(90)
        i = i + 1
    raphael.end_fill()


def starry_night(raphael: Turtle) -> None:
    """Sun in the sky and a person lying on the ground!"""
    circle(raphael, randint(-300, 300), randint(10, 250))
    rectangle(raphael, -10, -250)
    line(raphael, 25, -200)
    square(raphael, 100, -200)
    line(raphael, 75, -200)
    line(raphael, 95, -200)


def main() -> None:
    """The entrypoint of my scene."""
    raphael: Turtle = Turtle()
    starry_night(raphael)
    done()


if __name__ == "__main__":
    main()
