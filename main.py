from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

'''SCREEN SETUP'''

screen = Screen()
screen.setup(height=600, width=800)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)

'''PADDLE SETUP'''

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.onkey(paddle_r.up, key="Up")
screen.onkey(paddle_r.down, key="Down")
screen.onkey(paddle_l.up, key="w")
screen.onkey(paddle_l.down, key="s")
screen.listen()

game = True

'''score and collision setup'''
def Game():

    global game
    score_r = 0
    score_l = 0
    while game:
        time.sleep(0.1)
        screen.update()
        ball.move()
        if ball.ycor() > 270 or ball.ycor() < -270:
            ball.bounce()

        if paddle_r.distance(ball) < 20 or paddle_l.distance(ball) < 20:
            ball.down()
            print("hii")

        if (ball.xcor() >= 319 and paddle_r.distance(ball) <= 55) or (
                ball.xcor() <= -319 and paddle_l.distance(ball) <= 55):
            ball.down()
            print(paddle_r.distance(ball))
            print(paddle_l.distance(ball))
            print("kp")

        if ball.xcor() > 390 or ball.xcor() < -390:
            game = False

            if ball.xcor() > 390:
                score_l += 1
                score.score.clear()
                score.score_l(score_l)
                ball.down()

            if ball.xcor() < -390:
                score_r += 1
                score.score.clear()
                score.score_r(score_r)
                ball.down()
            screen.update()
            ball.refresh()
            paddle_l.refresh((-350, 0))
            paddle_r.refresh((350, 0))
            game = True


Game()
screen.exitonclick()
