from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, color):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.pu()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x=x_cor, y=0)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor()+20)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor()-20)
      
