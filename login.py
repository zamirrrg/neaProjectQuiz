
from tkinter import *
from tkinter import messagebox
import db
import mainmenu


class LoginWindow:

    def __init__(self):
        self.win = Tk()
        # reset the window and background color
        self.canvas = Canvas(self.win, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.uname = " "
        self.spw = " "

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
        self.win.title("WELCOME | Login Window | ADMINISTRATOR")

    def add_frame(self):
        self.frame = Frame(self.win, height=400, width=450)
        self.frame.place(x=80, y=50)

        x, y = 70, 20

        self.img = PhotoImage(file='images/login.png')
        self.label = Label(self.frame, image= self.img)
        self.label.place(x = x + 80, y = y + 0)

        #now create a login form
        self.label = Label(self.frame, text="Student Login")
        self.label.config(font=("Courier", 20, 'bold'))
        self.label.place(x=140, y = y + 150)

        self.uslabel = Label(self.frame, text="Enter Username")
        self.uslabel.config(font=("Courier", 12, 'bold'))
        self.uslabel.place(x=50, y= y + 230)

        self.username = Entry(self.frame, font='Courier 12')
        self.username.place(x=200, y= y + 230)

        self.pslabel = Label(self.frame, text="Enter Password")
        self.pslabel.config(font=("Courier", 12, 'bold'))
        self.pslabel.place(x=50, y=y+260)

        self.studentpassword = Entry(self.frame,show='*', font='Courier 12')
        self.studentpassword.place(x=200, y=y+260)

        self.button = Button(self.frame, text="Login", font='Courier 15 bold',
                             command=self.login)
        self.button.place(x=170, y=y + 290)

        self.win.mainloop()

    def login(self):
        #get the data and store it into tuple (data)

        data = (
            self.username.get(), self.studentpassword.get()
        )

        check = db.user_login(data)

        #validations
        if check == "Username incorrect":
            messagebox.showinfo("Username incorrect")
        elif check == "Password incorrect":
            messagebox.showinfo("Password incorrect")
        elif check == True:
                self.win.destroy()
                mainMenu = mainmenu.Mainmenu(data[0])
                mainMenu.add_frame()
        else: #check == False
            messagebox.showinfo("Login failure!")