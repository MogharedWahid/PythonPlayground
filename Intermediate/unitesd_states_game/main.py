import pandas
import turtle
from turtle import Turtle, Screen


FONT = ("Courier", 8, "bold")

def locate_state(data, state_name):
    state_data = data[data.state == state_name]
    new_state = Turtle()
    new_state.pu()
    new_state.hideturtle()
    new_state.goto(state_data.x.item(), state_data.y.item())
    new_state.write(answer_state, align='center', font=FONT)

states_data_frame = pandas.read_csv("50_states.csv")
all_states = states_data_frame['state'].to_list()

screen = Screen()
screen.title("United States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

correct_guesses = []
correct_guesses_count = 0

while correct_guesses_count < 50:
    answer_state = screen.textinput(f"{correct_guesses_count}/50 Correct States", prompt="Guess a state name").title()
    if answer_state == 'Exit':
        states_to_learn = [state for state in all_states if state not in correct_guesses]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv('states_to_learn.csv')
        break
    elif answer_state in all_states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        correct_guesses_count += 1
        locate_state(states_data_frame, answer_state)
