from tkinter import *
import pandas as pd
import random

# Load the data
try:
    data = pd.read_csv("Game Development/FlashCardMaster/data/french_words.csv")
except FileNotFoundError:
    data = pd.read_csv("Game Development/FlashCardMaster/words_to_learn.csv")
finally:
    words = data.to_dict(orient="records")

BACKGROUND_COLOR = "#B1DDC6"

# Function to flip the card and show the answer
def flip_card():
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(language_title, text="English", fill="White")
    canvas.itemconfig(word_text, text=selected_card["English"], fill="White")

# Function to display a new card
def show_new_card():
    global flip_timer
    global selected_card
    window.after_cancel(flip_timer)
    selected_card = random.choice(words)
    canvas.itemconfig(card_image, image=front_image)
    canvas.itemconfig(language_title, text="French", fill="black")
    canvas.itemconfig(word_text, text=selected_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)

# Function to handle correct answer
def mark_as_known():
    global selected_card
    global words
    words.remove(selected_card)
    new_data = pd.DataFrame(words)
    new_data.to_csv("Game Development/FlashCardMaster/words_to_learn.csv", index=False)
    show_new_card()

# Function to handle incorrect answer
def mark_as_unknown():
    show_new_card()

# Set up the main window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Cards")

# Set up the canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="Game Development/FlashCardMaster/images/card_front.png")
back_image = PhotoImage(file="Game Development/FlashCardMaster/images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_title = canvas.create_text(400, 160, text="French", font=("Ariel", 40, "italic"))
selected_card = random.choice(words)
word_text = canvas.create_text(400, 263, text=selected_card["French"], font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Set up the flip timer
flip_timer = window.after(3000, flip_card)

# Set up the buttons
wrong_image = PhotoImage(file="Game Development/FlashCardMaster/images/wrong.png")
right_image = PhotoImage(file="Game Development/FlashCardMaster/images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=mark_as_unknown)
right_button = Button(image=right_image, highlightthickness=0, command=mark_as_known)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

# Start the Tkinter event loop
window.mainloop()
