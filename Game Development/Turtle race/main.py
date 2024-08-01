from turtle import Turtle, Screen
import random
turtles = []
screen = Screen()
screen.setup(width=500, height=400)
color = ["red", "yellow", "orange", "green", "blue", "purple"]
count = 0
distance = 150/3
race_over = False
choice = screen.textinput(title= "Make your bet", prompt="Which turtle will win? Enter the color: ")
answer = ()



for i in color:
    tim = Turtle()
    turtles.append(tim)
    tim.color(i)
    tim.shape("turtle")
    tim.penup()
    if count<=3:
        tim.goto(-220, distance*count)
    else:
        tim.goto(-220,-distance*(count-3))
    count+=1
    
    
while not race_over:
    for turtle in turtles:
        move = random.randint(1,5)
        cor = int(turtle.xcor())
        if cor >=210:
            answer = turtle.color()
            race_over = True
            break
        turtle.goto(cor+move,turtle.ycor())
    
if choice == answer[0]:
    print("You won!")
else:
    print("You lost")
    print(f"Winner is: {answer[0]}")

screen.exitonclick()