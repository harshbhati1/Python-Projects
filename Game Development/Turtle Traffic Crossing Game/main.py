import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
board = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")
cars = []

looprun = 0

game_is_on = True
while game_is_on:
    looprun+=1
    
    if (looprun == 5):
        car = CarManager()
        cars.append(car)
        looprun = 0
        
    for car in cars:
        car.move()
        if (car.xcor() < -320):
            cars.remove(car)
    
    time.sleep(0.1)
    screen.update()
    
    if player.ycor() > 280:
        player.startAgain()
        car.increment()
        board.updateScore()
    
    for car in cars:
        if car.distance(player) < 30:
            game_is_on = False
            board.gameOver()
    
screen.exitonclick()        
        
