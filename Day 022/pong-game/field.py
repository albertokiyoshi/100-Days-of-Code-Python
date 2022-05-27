from turtle import Turtle


class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.pensize(5)
        self.goto(0, 295)
        self.pendown()
        self.setheading(270)
        for _ in range(1, 30):
            self.forward(10)
            self.penup()
            self.forward(12)
            self.pendown()
