from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.goto(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.moving_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.moving_speed = 0.1
      
