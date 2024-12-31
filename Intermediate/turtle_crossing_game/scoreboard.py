from turtle import Turtle

FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.pu()
        self.goto(-240, 270)
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', False, 'center', FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', False, 'center', FONT)
      
