from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.xcor() == 350:
            if not self.ycor() == 220:
                self.goto(350, self.ycor() + 20)
        else:
            if not self.ycor() == 220:
                self.goto(-350, self.ycor() + 20)

    def down(self):
        if self.xcor() == 350:
            if not self.ycor() == -220:
                self.goto(350, self.ycor() - 20)
        else:
            if not self.ycor() == -220:
                self.goto(-350, self.ycor() - 20)
                 
    def refresh(self, position):
        self.goto(position)




