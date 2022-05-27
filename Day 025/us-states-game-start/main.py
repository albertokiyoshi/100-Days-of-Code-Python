import turtle
import pandas
from scoreboard import Scoreboard

PROMPT = "What's another state's name?"

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

while scoreboard.score < 50:

    answer_state = screen.textinput(title=f"{scoreboard.score}/50 States Correct", prompt=PROMPT).title()

    if answer_state == "Exit":
        break

    if answer_state in states_list:
        scoreboard.raise_score()
        states_list.remove(answer_state)
        state_data = data[data.state == answer_state]
        position = (int(state_data.x), int(state_data.y))
        scoreboard.name_state(position, answer_state)

states_to_learn = pandas.DataFrame(states_list)
states_to_learn.to_csv("states_to_learn.csv")

screen.exitonclick()
