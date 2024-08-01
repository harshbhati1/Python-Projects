from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work = 0
counter = NONE
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    global work
    window.after_cancel(counter)
    reps = 0
    work = 0
    checkLabel.config(text=f"{"✓"*work}")
    canvas.itemconfig(time, text = "00:00")
    timerText.config(text="TIMER", fg = GREEN, font=(FONT_NAME, 40), bg=YELLOW)
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start():
    global reps
    global work
    WORK_SEC = WORK_MIN * 60
    SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_SEC = LONG_BREAK_MIN * 60
    reps+=1
    
    if reps % 8 == 0:
        countDown(count = LONG_BREAK_SEC)
        timerText.config(text="BREAK", fg = RED, font=(FONT_NAME, 40), bg=YELLOW)
    elif reps%2 == 0:
        countDown(count= SHORT_BREAK_SEC)
        timerText.config(text="BREAK", fg = PINK, font=(FONT_NAME, 40), bg=YELLOW)
        work+=1
        checkLabel.config(text=f"{"✓"*work}")
    else:
        countDown(count= WORK_SEC)
        
    
def countDown(count):
    global counter
    min = math.floor(count/60)
    sec = count % 60
    
    if sec < 10:
        sec = f"0{sec}"
        
    canvas.itemconfig(time, text = f"{min}:{sec}")
    if count >= 0 : 
       counter =  window.after(1000, countDown, count-1)
    else:
        start()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="Game Development/Pomodoro/tomato.png")
canvas.create_image(100,112, image = img, )
time = canvas.create_text(100,130, text="00:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)


timerText = Label(text="TIMER", fg = GREEN, font=(FONT_NAME, 40), bg=YELLOW)
timerText.grid(row=0,column=1)
startButton = Button(text="Start", command= start )
startButton.grid(row=2,column=0)
resetButton = Button(text="Reset", command= reset )
resetButton.grid(row=2,column=2)
checkLabel = Label(text=f"{"✓"*work}", fg = GREEN, font=(FONT_NAME, 10,"bold"), bg=YELLOW)
checkLabel.grid(row=2,column=1)




window.mainloop()