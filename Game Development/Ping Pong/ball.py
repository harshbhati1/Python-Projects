from turtle import *
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.goto(0,0)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.x_move = 0.08
        self.y_move = 0.08
        self.move_speed = 0.1
        
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)
    
    def bounceY(self):
        self.y_move*= -1
    
    def bounceX(self):
        self.x_move*=-1
        self.x_move*= 1.1
        self.y_move*=1.1
    
    def movingBack(self):
        self.goto(0,0)
        self.x_move = 0.08
        self.y_move = 0.08
        time.sleep(0.1)
        self.bounceX()
        
        