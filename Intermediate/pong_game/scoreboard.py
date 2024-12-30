from turtle import Turtle


FONT = ('Courier', 40, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.pu()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.left_score, align='center', font=FONT)
        self.goto(100, 220)
        self.write(self.right_score, align='center', font=FONT)
      
