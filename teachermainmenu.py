from tkinter import *
from tkinter import messagebox
import CS1Menu
import CS2Menu
import ME1Menu
import ME2Menu
import EC1Menu
import EC2Menu
import addnewstudent
import db

class TeacherMainMenu:

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
        self.win.title("MAIN MENU | QUIZU! | Teacher")

    def add_frame(self):

        # create a inner frame
        self.frame = Frame(self.win, height=300, width=450)
        self.frame.place(x=80, y=50)
        x, y = 70, 20
        self.labeltitle = Label(self.frame, text="QuizU!")
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(x=170, y=y + 10)


        self.button = Button(self.frame, text="CS1", font=('helvetica', 20, 'underline italic')
                                 , bg='purple', fg='white', command=self.CS1)
        self.button.place(x=40, y= 80)

        self.button = Button(self.frame, text="CS2", font=('helvetica', 20, 'underline italic')
                                 , bg='purple', fg='white', command=self.CS2)
        self.button.place(x=120, y= 80)

        self.button = Button(self.frame, text="ME1", font=('helvetica', 20, 'underline italic')
                                 , bg='purple', fg='white', command=self.ME1)
        self.button.place(x=40, y=140)

        self.button = Button(self.frame, text="ME2", font=('helvetica', 20, 'underline italic')
                             , bg='purple', fg='white', command=self.ME2)
        self.button.place(x= 120, y= 140)

        self.button = Button(self.frame, text="EC1", font=('helvetica', 20, 'underline italic')
                             , bg='purple', fg='white', command=self.EC1)
        self.button.place(x=40, y= 200)

        self.button = Button(self.frame, text="EC2", font=('helvetica', 20, 'underline italic')
                             , bg='purple', fg='white', command=self.EC2)
        self.button.place(x=120, y=200)

        self.button = Button(self.frame, text= "Add New Student",font=('helvetica', 20, 'underline italic')
                             ,bg='light blue', fg='black',command=self.newStudent)
        self.button.place(x=200, y=80)

        self.win.mainloop()

    def newStudent(self):
        self.win.destroy()
        ANS = addnewstudent.addNewStudent(self.username)
        ANS.startAddNewStudent()

    def CS1(self):
        check = db.class_check(self.username, "CS1")
        if check:
            self.win.destroy()
            cs1menu = CS1Menu.CS1Menu(self.username)
            cs1menu.add_frame()
        else:
            messagebox.showinfo("THIS IS NOT YOUR CLASS")

    def CS2(self):
        check = db.class_check(self.username, "CS2")
        if check:
            self.win.destroy()
            cs2menu= CS2Menu.CS2Menu(self.username)
            cs2menu.add_frame()
        else:
            messagebox.showinfo("THIS IS NOT YOUR CLASS")

    def ME1(self):
        check = db.class_check(self.username, "ME1")
        if check:
            self.win.destroy()
            me1menu = ME1Menu.ME1Menu(self.username)
            me1menu.add_frame()
        else:
            messagebox.showinfo("THIS IS NOT YOUR CLASS")

    def ME2(self):
        check = db.class_check(self.username, "ME2")
        if check:
            self.win.destroy()
            me2menu = ME2Menu.ME2Menu(self.username)
            me2menu.add_frame()
        else:
            messagebox.showinfo("THIS IS NOT YOUR CLASS")

    def EC1(self):
        check = db.class_check(self.username, "EC1")
        if check:
            self.win.destroy()
            ec1menu = EC1Menu.EC1Menu(self.username)
            ec1menu.add_frame()
        else:
            messagebox.showinfo("THIS IS NOT YOUR CLASS")

    def EC2(self):
        check = db.class_check(self.username, "EC2")
        if check:
            self.win.destroy()
            ec2menu = EC2Menu.EC2Menu(self.username)
            ec2menu.add_frame()
        else:
            messagebox.showinfo("THIS IS NOT YOUR CLASS")

