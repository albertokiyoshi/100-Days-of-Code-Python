from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [170, 102, 34, -34, -102, -170]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        distance = randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            is_race_on = False

if winner == user_bet:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")

screen.exitonclick()
