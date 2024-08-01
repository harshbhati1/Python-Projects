from turtle import *
import os

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.highscore = 0  # Default highscore if file doesn't exist or is invalid

        # Ensure data.txt exists with a default value of 0
        if not os.path.exists("Game Development/Snake Game/data.txt"):
            with open("Game Development/Snake Game/data.txt", mode="w") as file:
                file.write("0")

        # Try to read the highscore from the file
        try:
            with open("Game Development/Snake Game/data.txt", mode="r") as file:
                self.highscore = int(file.read().strip())
        except ValueError:
            self.highscore = 0  # In case the file content is not a valid integer

        self.goto(0, 260)
        self.color("White")
        self.hideturtle()
        self.penup()
        self.update()
    
    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Game Development/Snake Game/data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = -1
        self.update()
