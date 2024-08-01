from turtle import *
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.goto(x,y)
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.left(90)
        
    def moveUp(self):
        self.forward(40)
        
    def moveDown(self):
        self.backward(40)