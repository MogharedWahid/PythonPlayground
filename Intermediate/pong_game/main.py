import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

PADDLE_XCOR = 350

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Moghared Pong Game")
screen.bgcolor('black')
screen.tracer(0)

right_paddle = Paddle(PADDLE_XCOR, 'red')
left_paddle = Paddle(-PADDLE_XCOR, 'blue')
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

game_on = True
while game_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with paddle
    if ((ball.distance(right_paddle) < 50 and ball.xcor() > 320) or
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320)):
        ball.bounce_paddle()

    # Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score +=1
        scoreboard.update_score()

    # Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score += 1
        scoreboard.update_score()

screen.exitonclick()

