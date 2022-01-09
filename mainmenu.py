from tkinter import *
from tkinter import messagebox
import computersciencemenu
import economicsmenu
import mediamenu
import db


class Mainmenu:

    def __init__(self, username):
        self.win = Tk()
        self.username = username
        self.canvas = Canvas(self.win, width = 600 , height = 500 , bg = 'lavender')
        self.canvas.pack(expand = YES , fill = BOTH)

        # show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+" + str(x) + "+" + str(y)
        self.win.geometry(str1)

        # disable resize of the window
        self.win.resizable(width=False, height=False)


        #change the title of the window
        self.win.title("MAIN MENU | QUIZU! | ADMINISTRATOR")

    def add_frame(self):
        # create a inner frame
        self.frame = Frame(self.win, height=300, width=450)
        self.frame.place(x=80, y=50)
        x, y = 70, 20
        self.labeltitle = Label(self.frame, text="QuizU!")
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(x=170, y=y + 10)


        self.button = Button(self.frame, text="Computer Science", font=('helvetica', 20, 'underline italic')
                                 , bg='purple', fg='white', command=self.ComputerScienceCheck)
        self.button.place(x=x + 40, y=y + 80)

        self.button = Button(self.frame, text="Economics", font=('helvetica', 20, 'underline italic')
                                 , bg='purple', fg='white', command=self.EconomicsCheck)
        self.button.place(x=x + 80, y=y + 150)

        self.button = Button(self.frame, text="Media", font=('helvetica', 20, 'underline italic')
                                 , bg='purple', fg='white', command=self.MediaCheck)
        self.button.place(x=x + 110, y=y + 220)

        self.win.mainloop()

    def ComputerScienceCheck(self):
        check = db.subject_check(self.username)
        if check == "Computer science":
            self.win.destroy()
            log = computersciencemenu.CSMenu(self.username)
            log.add_frame()
        else:
            messagebox.showinfo("YOU ARE NOT IN THIS CLASS")

    def EconomicsCheck(self):
        check = db.subject_check(self.username)
        if check == "Economics":
            self.win.destroy()
            log = economicsmenu.ECMenu(self.username)
            log.add_frame()

        else:
            messagebox.showinfo("YOU ARE NOT IN THIS CLASS")


    def MediaCheck(self):
        check = db.subject_check(self.username)
        if check == "Media":
            self.win.destroy()
            log = mediamenu.MEMenu(self.username)
            log.add_frame()
        else:
            messagebox.showinfo("YOU ARE NOT IN THIS CLASS")

