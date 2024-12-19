import random
from turtle import Turtle, Screen

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
racer_turtles = []

def create_turtles():
    y = -100
    for color in colors:
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(color)
        racer_turtles.append(new_turtle)
        new_turtle.pu()
        new_turtle.goto(x=-230, y=y)
        y += 40

create_turtles()

if user_bet:
    race_on = True

while race_on:
    for turtle in racer_turtles:
        if turtle.xcor() >= 230:
            if turtle.pencolor() == user_bet:
                print(f"YOU WIN 😎. The {user_bet} turtle won the race!")
            else:
                print(f"YOU LOST 😭. The {turtle.pencolor()} turtle won the race!")
            race_on = False
            break
        random_step = random.randint(0,5)
        turtle.forward(random_step)



screen.exitonclick()
