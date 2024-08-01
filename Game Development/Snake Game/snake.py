from turtle import *
import time

class Snake:
    def __init__(self):
        self.body = []
        position = [(0,0), (-20,0), (-40,0)]
        
        for i in range(3):
            turt = Turtle()
            turt.shape("square")
            turt.color("white")
            turt.penup()
            turt.goto(position[i])
            self.body.append(turt)
            
            
    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            x = self.body[i-1].xcor()
            y = self.body[i-1].ycor()
            self.body[i].goto(x,y)
        self.body[0].forward(20)
    
    def increase(self):
         turt = Turtle()
         turt.shape("square")
         turt.color("white")
         turt.penup()
         turt.goto(self.body[-1].position())
         self.body.append(turt)
    
    def reset(self):
        for i in self.body:
            i.goto(1000,1000)
        
        self.body.clear()
        self.__init__()
        
            
        
    
    def up(self):
        if self.body[0].heading()!=270:
            self.body[0].setheading(90)
        
    def down(self):
        if self.body[0].heading()!=90:
            self.body[0].setheading(270)
    
    def left(self):
        if self.body[0].heading()!=0:
            self.body[0].setheading(180)
    
    def right(self):
         if self.body[0].heading()!=180:
            self.body[0].setheading(0)
        
        