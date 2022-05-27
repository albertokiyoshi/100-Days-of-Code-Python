from turtle import Turtle

FONT = ("Arial", 10, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0

    def name_state(self, position, state_name):
        self.goto(position)
        self.write(state_name, align="center", font=FONT)

    def raise_score(self):
        self.score += 1