from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
