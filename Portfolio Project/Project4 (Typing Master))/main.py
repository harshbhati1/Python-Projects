import tkinter as tk
import random

# Function to start the timer
def start_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Timer: {time_left:02}")
        root.after(1000, start_timer)
    elif time_left == 0:
        calculate_wpm()

# Function to calculate Words Per Minute (WPM)
def calculate_wpm():
    global correctWords
    global time_left
    wpm_label.config(text=f"WPM: {correctWords * 60 // (60 - time_left)}")

# Function to count correct words
def correctWordCounter(answer):
    global correctWords
    global words
    answerList = answer.split(' ')
    copylist = words.copy()
    correct = 0
    
    for i in answerList:
        if i in copylist:
            correct += 1
            copylist.remove(i)

    correctWords = correct

# Function to update and print user input in real-time
def on_key_release(event):
    input_text = user_input.get()
    calculate_wpm()
    correctWordCounter(input_text)
    correct_words_label.config(text=f"Correct Words: {correctWords}/{len(words)}")
    update_text_color(input_text)
    
# Function to update the text color of each letter in the question
def update_text_color(input_text):
    global time_left
    text_label.config(state=tk.NORMAL)  # Temporarily enable editing to update color
    text_label.delete("1.0", tk.END)  # Clear text box for fresh update

    input_index = 0

    for char in text_to_type:
        if char == " ":
            text_label.insert(tk.END, char, "normal")
            input_index += 1
        else:
            if input_index < len(input_text):
                if input_text[input_index] == char:
                    text_label.insert(tk.END, char, "correct")
                else:
                    text_label.insert(tk.END, char, "incorrect")
                input_index += 1
            else:
                text_label.insert(tk.END, char, "normal")

    # Reapply center alignment
    text_label.tag_add('center', '1.0', 'end')

    if correctWords == len(words):
        calculate_wpm()
        time_left = -1
        entry.config(state=tk.DISABLED)

    text_label.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Typing Test")

# Variables
time_left = 60  # 1 minute timer
total_time = time_left

# Labels and layout
with open('Portfolio Project\Project4 (Typing Master))\questions.txt') as file:
    lines = file.readlines()
    text_to_type = random.choice(lines)
    text_to_type = random.choice(lines).strip()

words = text_to_type.split(' ')

correctWords = 0

# Style configuration for black and white theme
bg_color = "#000000"
fg_color = "#FFFFFF"
correct_color = "green"
incorrect_color = "red"

root.configure(bg=bg_color)

correct_words_label = tk.Label(root, text=f"Correct Words: {correctWords}/{len(words)}", bg=bg_color, fg=fg_color, font=('Arial', 12))
correct_words_label.pack(pady=10)

timer_label = tk.Label(root, text=f"Timer: {time_left:02}", bg=bg_color, fg=fg_color, font=('Arial', 12))
timer_label.pack(pady=10)

wpm_label = tk.Label(root, text="WPM: N/A", bg=bg_color, fg=fg_color, font=('Arial', 12))
wpm_label.pack(pady=10)

question_label = tk.Label(root, text="Type the following text:", bg=bg_color, fg=fg_color, font=('Arial', 14))
question_label.pack(pady=10)

# Text widget to display the question
text_label = tk.Text(root, height=1, width=len(text_to_type), font=('Arial', 16), bg=bg_color, fg=fg_color, bd=0)
text_label.tag_configure('center', justify='center')
text_label.pack(pady=10, padx=20)
text_label.insert(tk.END, text_to_type, "normal")
text_label.tag_add('center', '1.0', 'end')

# Configure tags for text colors
text_label.tag_configure("correct", foreground=correct_color)
text_label.tag_configure("incorrect", foreground=incorrect_color)
text_label.tag_configure("normal", foreground=fg_color)

# Initially display the question text
text_label.config(state=tk.DISABLED)  # Make the text widget read-only

# Input box
user_input = tk.StringVar()
entry = tk.Entry(root, textvariable=user_input, font=('Arial', 16), bg=bg_color, fg=fg_color, bd=2, insertbackground=fg_color)
entry.pack(pady=10, padx=20)

# Bind the key release event to the input box
entry.bind('<KeyRelease>', on_key_release)

# Start the timer
start_timer()

root.mainloop()