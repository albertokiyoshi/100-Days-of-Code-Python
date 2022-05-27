from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.level = 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.display_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align="center", font=FONT)
