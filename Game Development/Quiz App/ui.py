from tkinter import *
from quiz_brain import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(height=600, width=400,padx=20, pady=20, bg= THEME_COLOR)
        
        self.label = Label(text = f"Score: {self.score}", font= ("Aerial", 14), fg="white", bg=THEME_COLOR)
        self.label.grid(row=0,column=1)
        
        self.canvas = Canvas(width=300, height=250, bg= "white")
        self.questionText = self.canvas.create_text(150,125,width=280, text="qqqq", font= ("Aerial", 20, "italic"))
        self.canvas.grid(row=1, columnspan=2, pady=50)
        
        
        self.rightImage = PhotoImage(file="Game Development/Quiz App/images/true.png")
        self.rightButton = Button(image=self.rightImage, highlightthickness=0, command= self.right)
        self.rightButton.grid(row=2, column=0)
        
        self.leftImage = PhotoImage(file="Game Development/Quiz App/images/false.png")
        self.leftButton = Button(image=self.leftImage, highlightthickness=0, command= self.left)
        self.leftButton.grid(row=2, column=1)
        
        self.nextQuestion()
        
        
        self.window.mainloop()
    
    def nextQuestion(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            global quest
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text = q_text)
        else:
            self.canvas.itemconfig(self.questionText, text = "You've reached the end!")
            self.rightButton.config(state="disabled")
            self.leftButton.config(state="disabled")
    
    def right(self):
        self.giveFeedback(self.quiz.check_answer("True"))
        
    
    def left(self):
        self.giveFeedback(self.quiz.check_answer("False"))  
    
    def giveFeedback(self,isRight):
        
        if isRight:
            self.score+=1
            self.label.config(text= f"Score: {self.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000,self.nextQuestion)
        
        
        