from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.y_direction = choice(["up", "down"])
        self.x_direction = choice(["right", "left"])
        self.speed = 1

    def move(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.bounce_y()

        new_x = self.xcor() + self.x_move * self.speed
        new_y = self.ycor() + self.y_move * self.speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def centralize(self):
        self.goto(0, 0)
        self.bounce_x()
        self.speed = 1

    def increase_speed(self):
        self.speed += 0.1
