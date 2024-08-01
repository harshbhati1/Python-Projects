from turtle import *
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.writeScore()
    
    def writeScore(self):
        self.clear()
        self.goto(-210,240)
        self.write(f"Score: {self.score}", align="center", font= ("Courier", 24, "normal"))
    
    def updateScore(self):
        self.score+=1
        self.writeScore()
    
    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font= ("Courier", 50, "normal"))
                
        
        
        
    
