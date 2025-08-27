
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzlerApp():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.root = Tk()
        self.root.title("Quizzler")
        # self.geometry("400x400")
        self.root.configure(bg=THEME_COLOR,padx=20,pady=20)
        self.score_label=Label(text="Score:",fg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(self.root,bg="white",width=300,height=250)
        self.text=self.canvas.create_text(150,125,width=280,text="Score:",fill=THEME_COLOR,font=("Times New Roman",20))

        self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)
        self.image=PhotoImage(file="./images/false.png")
        self.image1=PhotoImage(file="./images/true.png")
        self.button=Button(self.root,image=self.image,command=self.false_pressed)
        self.button.grid(row=2,column=0,padx=20,pady=20)
        self.button1=Button(self.root,image=self.image1,command=self.true_pressed)
        self.button1.grid(row=2,column=1,padx=20,pady=20)
        # self.minsize(400, 400)
        # self.maxsize(400, 400)

        self.get_next_question()
        self.root.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            next_q=self.quiz.next_question()
            self.canvas.itemconfig(self.text,text=next_q)
        else:
            self.canvas.itemconfig(self.text,text="YOU HAVE REACHED THE END QUESTION")
            self.button.config(state="disabled")
            self.button1.config(state="disabled")

    def true_pressed(self):
        self.get_feedback(self.quiz.check_answer("True"))
        # self.canvas.itemconfig(self.text,bg="green")
    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.get_feedback(is_right)
        # self.canvas.itemconfig(self.text,bg="red")
    # def change_color(self):
    #     self.canvas.itemconfig(self.text,bg="white")
    def get_feedback(self,is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000,self.get_next_question)



