from turtle import *
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0,-280)
        self.left(90)
    
    def move(self):
        self.forward(10)
    
    def startAgain(self):
        self.goto(0,-280)
        
