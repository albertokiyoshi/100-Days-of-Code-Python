import turtle
from turtle import Turtle, Screen
from random import choice, randint

turtle.colormode(255)
timmy = Turtle()
timmy.speed(0)
directions = [0, 90, 180, 270]


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = (red, green, blue)
    return color


def shapes():
    for faces in range(2, 11):
        timmy.color(random_color())
        angle = 360 / faces
        n = 360 / angle
        for _ in range(int(n)):
            timmy.fd(100)
            timmy.right(angle)


def random_walk():
    for _ in range(200):
        timmy.color(random_color())
        timmy.setheading(choice(directions))
        timmy.forward(30)


def spirograph():
    for _ in range(144):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.left(2.5)

spirograph()

screen = Screen()
screen.exitonclick()

