from turtle import Turtle
FONT_1 = ("Courier", 50, "bold")
FONT_2 = ("Courier", 25, "bold")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 220)
        self.color("white")
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"{self.player_1_score}      {self.player_2_score}", align=ALIGNMENT, font=FONT_1)

    def player_1_point(self):
        self.player_1_score += 1
        self.refresh()

    def player_2_point(self):
        self.player_2_score += 1
        self.refresh()

    def game_over(self, winner):
        self.refresh()
        self.goto(-200, 0)
        self.write("Game over!", align=ALIGNMENT, font=FONT_2)
        self.goto(200, 0)
        self.write(f"{winner} wins.", align=ALIGNMENT, font=FONT_2)

