import tkinter
from tkinter import *
from tkinter import ttk
import db
import math

class QuizUI:

    def __init__(self, quiz, username, topic):

        self.username = username
        self.quiz = quiz
        self.topic = topic

        self.win = tkinter.Tk()
        self.canvas = Canvas(self.win, width=1280, height=1024, bg='lavender')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.score = 0

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("QUIZU!")

    def startQuizInner(self, canvas, i):
        if canvas is not None:
            canvas.destroy()

        if i < len(self.quiz):
            q = self.quiz[i][0]
            a = self.quiz[i][1]
            wa1 = self.quiz[i][2]
            wa2 = self.quiz[i][3]

            questionCanvas = Canvas(self.canvas, width=1280, height=1024, bg='lavender')
            questionCanvas.pack(expand=YES, fill=BOTH)

            # questions
            qlabel = Label(questionCanvas, text=q)
            qlabel.config(font=("Arial", 14, 'bold'))
            qlabel.config(bg="lavender",fg="black")
            qlabel.place(x=120, y=10)

            # answer + wrong answers with radio buttons

            chosen = StringVar()

            R1 = ttk.Radiobutton(questionCanvas, text=a, value='answer', variable=chosen)
            R1.pack(fill='x', padx=100, pady=55)
            R2 = ttk.Radiobutton(questionCanvas, text=wa1, value='wa1', variable=chosen)
            R2.pack(fill='x', padx=100, pady=55)
            R3 = ttk.Radiobutton(questionCanvas, text=wa2, value='wa2', variable=chosen)
            R3.pack(fill='x', padx=100, pady=55)

            button = Button(questionCanvas, text="Next Question", width=12, bg="purple", fg="white",
                            font=("arial", 12), command=(lambda: self.checkAnswer(questionCanvas, i, chosen)))
            button.place(x=130, y=380)

            quitButton = Button(questionCanvas, text="Quit", command=self.win.destroy, width=12, bg="red",
                                fg="white",
                                font=("arial", 12))
            quitButton.place(x=310, y=380)

        else:
            self.quizDone()

    def checkAnswer(self, canvas, i, chosen):
        value = chosen.get()

        # if the value returned is true
        if value == 'answer':
            self.score = self.score + 1

        self.startQuizInner(canvas, i + 1)

    def calculateScorePercentage(self):
        questionAmount = db.getQuestionAmount(self.topic)
        self.score = (self.score / questionAmount) * 100
        return self.score

    def quizDone(self):

        self.calculateScorePercentage()
        db.addScoreToDB(self.username, self.score, self.topic)

        # show score using a label
        tempStr = "You scored: " + str(math.trunc(self.score))

        showScore = Label(self.canvas, text=tempStr + "%")
        showScore.config(font=("Arial", 14, 'bold'))
        showScore.config(bg="purple", fg="white")
        showScore.place(x=200, y=20)

        quitButton = Button(self.canvas, text="Quit", command=self.canvas.destroy, width=12, bg="red",
                            fg="white",
                            font=("arial", 12))
        quitButton.place(x=310, y=380)