from turtle import Turtle, Screen

# Initialize Turtle and Screen objects
tim = Turtle()
screen = Screen()

# Function to move the turtle forward
def move_forwards():
    tim.forward(10)

# Function to move the turtle backward
def move_backwards():
    tim.backward(10)  # Updated to 'backward' for clarity

# Function to turn the turtle clockwise
def clockwise():
    tim.right(10)

# Function to turn the turtle counter-clockwise
def counter_clockwise():
    tim.left(10)

# Function to clear the screen and reset the turtle
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Set up key bindings
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

# Exit on screen click
screen.exitonclick()
