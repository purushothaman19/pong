from turtle import Turtle, Screen

screen = Screen()
POSITION = (-330, 20)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.x = 15
        self.y = 15

    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.x, y + self.y)

    def bounce(self):
        self.y *= -1

    def down(self):
        self.x *= -1

    def refresh(self):
        self.home()

    # def up(self):
    #     self.x *= 1
    #     self.y *= 1