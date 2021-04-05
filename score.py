from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.score = Turtle()
        self.score.color("white")
        self.score.ht()
        self.score.penup()
        self.setpos(250, 250)
        self.write(f"Player-1\nScore:", align="center", font=("Arial", 20, "normal"))
        self.setpos(-250, 250)
        self.write(f"Player-2\nScore:", align="center", font=("Arial", 20, "normal"))

    def score_r(self, score):
        self.score.setpos(240, 240)
        self.score.write(f"{score}", align="right", font=("Arial", 20, "normal"))

    def score_l(self, score):
        self.score.setpos(-210, 250)
        self.score.write(f"{score}", align="right", font=("Arial", 20, "normal"))
