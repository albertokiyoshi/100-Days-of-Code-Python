from colorgram import extract
from random import choice
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

paint = Turtle()
paint.speed(0)
paint.penup()
paint.setpos(-225, -225)
paint.hideturtle()


def colors_from_image():
    colors = extract("hirst.jpg", 42)
    rgb_colors = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))


def paint_row():
    for _ in range(10):
        paint.dot(20, choice(color_list))
        paint.forward(50)


color_list = [(28, 108, 162), (191, 40, 81), (233, 160, 57), (233, 214, 89), (220, 137, 175), (141, 108, 58),
              (107, 193, 215), (21, 57, 131), (202, 165, 33), (210, 73, 94), (236, 90, 56), (142, 29, 72),
              (119, 191, 142), (142, 208, 227), (9, 184, 170), (106, 107, 196), (7, 158, 86), (97, 51, 37),
              (22, 160, 206), (232, 166, 185), (85, 46, 34), (32, 46, 87), (151, 214, 197), (30, 87, 92),
              (234, 174, 163), (174, 184, 220), (242, 204, 6), (93, 27, 54), (32, 91, 91)]

for _ in range(10):
    paint_row()
    paint.left(90)
    paint.forward(50)
    paint.left(90)
    paint.forward(500)
    paint.left(180)

screen = Screen()
screen.exitonclick()
