import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

FOOD_COLLISION = 15
WALL_COLLISION_COR = 285
TAIL_COLLISION = 10

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor('black')
screen.title("Moghared Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

GAME_ON = True
while GAME_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < FOOD_COLLISION:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    #Detect collision with wall.
    if (snake.head.xcor() > WALL_COLLISION_COR or
            snake.head.xcor() < -WALL_COLLISION_COR or
            snake.head.ycor() > WALL_COLLISION_COR or
            snake.head.ycor() < -WALL_COLLISION_COR):
        score_board.game_over()
        GAME_ON = False

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < TAIL_COLLISION:
            score_board.game_over()
            GAME_ON = False




screen.exitonclick()
