from turtle import Turtle

SCORE_X_COR = 0
SCORE_Y_COR = 280
DEFAULT_SCORE = 0
CENTER = 0
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = DEFAULT_SCORE
        self.pu()
        self.color('white')
        self.goto(SCORE_X_COR, SCORE_Y_COR)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(CENTER, CENTER)
        self.color('red')
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
      
