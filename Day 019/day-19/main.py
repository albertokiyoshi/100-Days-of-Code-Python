from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_clockwise():
    tim.right(5)


def rotate_counterclockwise():
    tim.left(5)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_clockwise, "d")
screen.onkey(rotate_counterclockwise, "a")
screen.onkey(clear, "c")


screen.exitonclick()