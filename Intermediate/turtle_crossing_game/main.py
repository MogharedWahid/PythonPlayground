import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

iteration = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Turtle Crossing Game")
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    # Create a car every 6 iterations
    iteration += 1
    if iteration >= 6:
        iteration = 0
        car_manager.create_car()

    # Moving the cars
    car_manager.move_cars(scoreboard.level)

    # Check if turtle collides with car
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()
            break

    time.sleep(0.1)
    screen.update()

    # Check turtle reaches the other side
    if player.ycor() >= 280:
        scoreboard.update_scoreboard()
        player.reset_position()

screen.exitonclick()
