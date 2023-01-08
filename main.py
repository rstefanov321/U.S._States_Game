import turtle
import pandas
from state import State
from win import Winner


data = pandas.read_csv("50_states.csv")

data_state = data["state"]


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_on = True
score_states = 0
guessed_states = []

while game_on:
    answer_state = screen.textinput(title=f"{score_states} / 50 Guessed Correctly",
                                    prompt="What's another state's name? Write 'exit' to stop").title()
    # Some test prints:
    # print(answer_state)
    # print(type(answer_state))
    # print("****")
    # print(data[data.state == answer_state])
    # print("/////")

    if answer_state in list(data_state):
        chosen_state = data[data.state == answer_state]
        imp_x = int(chosen_state.x)
        # print(imp_x)
        imp_y = int(chosen_state.y)
        # print(imp_y)
        # or chosen_state.state.item()
        state = State(answer_state, imp_x, imp_y)
        score_states += 1
        guessed_states.append(answer_state)

    if score_states == 50:
        image = "winner_gif.gif"
        screen.addshape(image)
        turtle.shape(image)
        winner = Winner()
        game_on = False

    if answer_state == "Exit":
        break

missing_states = []
for i in data.state:
    if i not in guessed_states:
        missing_states.append(i)

states_to_learn = {
    "Missing States": missing_states
}

data_df = pandas.DataFrame(states_to_learn)
data_df.to_csv("states_to_learn.csv")
print("Please see the CSV file states_to_learn to see which states you have missed and should learn :) ")


