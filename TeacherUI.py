from tkinter import *
import db

class TeacherUI:
    def __init__(self, username, topic):
        self.win = Tk()
        self.username = username
        self.canvas = Canvas(self.win, width=600, height=500, bg='lavender')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.topic = topic

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("QUIZU! | Teacher")

    def startAddQ(self):

        myQ = StringVar()
        myA = StringVar()
        myWA1 = StringVar()
        myWA2 = StringVar()

        label = Label(self.canvas, text="Question: ")
        label.config(font=("Arial", 15, "bold"))
        label.config(bg="lavender", fg="black")
        label.place(x=40, y=10)

        addq = Entry(self.canvas, font="Arial 12", textvariable=myQ)
        addq.place(x=220, y=12)

        label = Label(self.canvas, text="Answer: ")
        label.config(font=("Arial", 15, "bold"))
        label.config(bg="lavender", fg="black")
        label.place(x=40, y=80)

        adda = Entry(self.canvas, font="Arial 12", textvariable=myA)
        adda.place(x=220, y=82)

        label = Label(self.canvas, text="Wrong answer 1: ")
        label.config(font=("Arial", 15, "bold"))
        label.config(bg="lavender", fg="black")
        label.place(x=40, y=150)

        wronga1 = Entry(self.canvas, font="Arial 12", textvariable=myWA1)
        wronga1.place(x=220, y=152)

        label = Label(self.canvas, text="Wrong answer 2: ")
        label.config(font=("Arial", 15, "bold"))
        label.config(bg="lavender", fg="black")
        label.place(x=40, y=220)

        wronga2 = Entry(self.canvas, font="Arial 12", textvariable=myWA2)
        wronga2.place(x=220, y=222)

        q = myQ.get()
        a = myA.get()
        wa1 = myWA1.get()
        wa2 = myWA2.get()

        print("qqqq: " + str(q))
        print("aaaa: " + str(a))
        print("waaa1: " + str(wa1))
        print("waaa2: " + str(wa2))

        add = Button(self.canvas, text="Add", font="Arial 14", command=(lambda: self.addButton(q, a, wa1, wa2)))
        add.config(bg="red", fg="white")
        add.place(x=130, y=300)

        quitButton = Button(self.canvas, text="Quit", command=self.win.destroy, width=12, bg="red",
                            fg="white",
                            font=("arial", 12))
        quitButton.place(x=310, y=300)

    def addButton(self, q, a, wa1, wa2):
        db.addQuestion(q, a, wa1, wa2, self.topic)


