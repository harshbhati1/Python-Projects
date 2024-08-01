from turtle import *

class Writer(Turtle):
    def __init__(self, word, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.write(word, align="center", font= ("Courier", 5, "normal"))
        
        