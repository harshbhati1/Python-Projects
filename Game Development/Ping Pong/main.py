from turtle import *
from paddle import *
from ball import *
from scoreboard import *
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

paddle1 = Paddle(350,0)
padddle2 = Paddle(-350, 0)
ball = Ball()
score = Scoreboard() 
screen.listen()
screen.onkey(paddle1.moveUp, "Up")
screen.onkey(paddle1.moveDown, "Down")
screen.onkey(padddle2.moveUp, "w")
screen,onkey(padddle2.moveDown, "s")

gameIsOn = True
while gameIsOn:
    screen.update()
    ball.move()
    
    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounceY()
    
    if (ball.distance(paddle1) < 50 and ball.xcor() > 340 or ball.distance(padddle2) < 50 and ball.xcor() < -340):
        ball.bounceX()
    
    if (ball.xcor()> 390):
        ball.movingBack()
        score.updateLscore()
    
    if (ball.xcor() < -390):
        ball.movingBack()
        score.updateRscore()

screen.exitonclick()