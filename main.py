from turtle import Turtle, Screen
import time
import random
from scoreboard import Score
score=Score()
from paddle import Paddle
from ball import Ball
ball = Ball()
#paddle=Turtle()
screen=Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
# paddle.penup()
#
# paddle.goto(350,0)
#
# paddle.shape("square")
# paddle.shapesize(7,1.5)
# paddle.fillcolor("white")
screen.listen()
r_paddle=Paddle((370,0))
l_paddle=Paddle((-380,0))


screen.onkeypress(r_paddle.f,"Up")
screen.onkeypress(r_paddle.d,"Down")
screen.onkeypress(l_paddle.f,"w")
screen.onkeypress(l_paddle.d,"s")




# move=True
#
# while move:
#     randomx = random.randint(10, 780)
#     randomy = random.randint(10, 580)
#     time.sleep(1)
#     screen.update()
#     ball.setposition(randomx,randomy)

game_on=True
i=0.1
while game_on:
    time.sleep(i)
    screen.update()
    ball.ball_move()
    if ball.ycor() >= 285 or ball.ycor()<=-285:

        ball.bounce_y()

        i*=0.9
    if ball.xcor()>340 and ball.distance(r_paddle)<50 or ball.xcor()<-350 and ball.distance(l_paddle)<50:
        ball.bounce_x()
        i *=0.9
    if ball.xcor() > 370 and ball.distance(r_paddle) > 50:
        ball.ball_ini()
        score.update_l()

    if ball.xcor() < -370 and  ball.distance(l_paddle) > 50:
        ball.ball_ini()
        score.update_r()
        i=0.1






screen.exitonclick()