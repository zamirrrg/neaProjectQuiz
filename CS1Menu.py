from tkinter import *
import TeacherUI
import db


class CS1Menu:

    def __init__(self,username):
        self.username = username
        self.win = Tk()
        self.canvas = Canvas(self.win, width=300, height=300, bg='lavender')
        self.canvas.pack(expand=YES, fill=BOTH)

        #center the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)

        # change the title of the window
        self.win.title("QUIZU! | CS1 MENU | Teacher")

    def add_frame(self):
        height = 400
        width = 400

        topicList = db.get_topics("cs_topics", "cs_topicID")

        count = 1
        for i in topicList:
            newButton = Button(self.win, text=i, font=('helvetica', 15, 'underline italic'), bg='purple',
                                   fg='white', command=(lambda : self.goToQuizUI(self.username, i)))

            newButton.place(x=width / 2, y=(height / len(topicList) * count))
            count = count + 1

        self.win.mainloop()

    def goToQuizUI(self, username, topic):
        teacherUI = TeacherUI.TeacherUI(username, topic)
        teacherUI.startAddQ()