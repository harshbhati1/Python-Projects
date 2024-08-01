from writer import *
import turtle
import pandas


# loading data 
data = pandas.read_csv("Game Development/US state game/50_states.csv")
# working 
guessedStates = 0
list = []

screen  = turtle.Screen()
screen.title("US State Game")
image = "Game Development/US state game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while guessedStates <= 50:
    user_input = screen.textinput(title= f"{guessedStates}/50", prompt="What's another state's name?").title()
    if user_input in data['state'].to_list():
        info = data[data["state"] == user_input]
        terp = Writer(user_input, info['x'].values[0],  info['y'].values[0])
        list.append(user_input)
        guessedStates+=1
    
    if user_input == "Exit":
        states = data["state"].to_list()
        missing_states = [state for state in states if state not in list]
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Game Development/US state game/states_to_learn.csv")
        break
        
    

turtle.mainloop()