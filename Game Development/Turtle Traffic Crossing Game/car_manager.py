from turtle import *
import random


class CarManager(Turtle):
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    STARTING_MOVE_DISTANCE = 5
    MOVE_INCREMENT = 10
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len= 2)
        self.color(random.choice(self.COLORS))
        self.goto(310, random.randint(-250, 250))
        
    def move(self):
        self.backward(self.STARTING_MOVE_DISTANCE)
    
    def increment(self):
        CarManager.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
        
        
