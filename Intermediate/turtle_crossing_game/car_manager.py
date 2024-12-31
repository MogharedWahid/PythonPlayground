import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car= Turtle('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.pu()
        new_car.goto(300, random.randint(-250,250))
        self.all_cars.append(new_car)

    def move_cars(self, level):
        level -= 1
        x_decrement = STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT
        for car in self.all_cars:
            car.goto(car.xcor()-x_decrement, car.ycor())
          
