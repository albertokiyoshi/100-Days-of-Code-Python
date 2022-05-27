from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from field import Field
import time


def centralize():
    ball.centralize()
    player_1.centralize()
    player_2.centralize()
    time.sleep(2)


screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()
field = Field()

screen.listen()
screen.onkeypress(player_1.go_up, "w")
screen.onkeypress(player_1.go_down, "s")
screen.onkeypress(player_2.go_up, "Up")
screen.onkeypress(player_2.go_down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.03)
    ball.move()

    if ball.distance(player_1) <= 55 and ball.xcor() <= -331 or ball.distance(player_2) <= 55 and ball.xcor() >= 330:
        ball.bounce_x()
        ball.increase_speed()

    if ball.xcor() > 400:
        scoreboard.player_1_point()
        centralize()
    if ball.xcor() < -400:
        scoreboard.player_2_point()
        centralize()

    if scoreboard.player_1_score > 2:
        scoreboard.game_over("Player 1")
        game_on = False
    elif scoreboard.player_2_score > 2:
        scoreboard.game_over("Player 2")
        game_on = False

screen.exitonclick()
