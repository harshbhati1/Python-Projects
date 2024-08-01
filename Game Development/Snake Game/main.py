from turtle import *
from snake import *
import time
from food import *
from board import *

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Snake Game")
    
gameIsOn = True
snake = Snake()
food = Food()
board = Board()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.body[0].distance(food) < 15:
        food.refresh() 
        board.update()
        snake.increase()
    
    if snake.body[0].xcor() > 290 or snake.body[0].xcor() < -290 or snake.body[0].ycor() > 290 or snake.body[0].ycor() < -290:
        board.reset()
        snake.reset()
    
    for positions in snake.body[1:]:
        
        if snake.body[0].distance(positions) < 10:
            board.reset()
            snake.reset()
   
    









screen.exitonclick()