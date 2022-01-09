
from tkinter import *
import login
import teacherlogin

class WelcomeWindow:

    #create a constructor
    def __init__(self):
        # create a tkinter window
        self.win = Tk()

        #reset the window and background color
        self.canvas = Canvas(self.win, width=600, height=400, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        #show window in center of the screen
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        #disable resize of the window
        self.win.resizable(width=False, height=False)

        #change the title of the window
        self.win.title("WELCOME | QUIZU! | ADMINISTRATOR")

    def add_frame(self):
        #create a inner frame
        self.frame = Frame(self.win, height=300, width=450)
        self.frame.place(x=80, y=50)

        x, y = 70, 20

        # place the photo in the frame

        self.img = PhotoImage(file='images/icon.png')
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x+80, y=y+0)

        self.labeltitle = Label(self.frame, text="Welcome to QuizU!")
        self.labeltitle.config(font=("Courier", 20, 'bold'))
        self.labeltitle.place(x=80, y=y+145)

        self.button = Button(self.frame, text="Teacher", font=('Arial', 20)
                             , bg='purple', fg='white', command=self.teacher_login)
        self.button.place(x=x + 20, y=y + 200)

        self.button = Button(self.frame, text="Student", font=('Arial', 20)
                             , bg='purple', fg='white', command=self.login)
        self.button.place(x=x + 180, y=y + 200)



        self.win.mainloop()

    #open a new window on button press
    def login(self):
        # destroy current window
        self.win.destroy()

        #open the new window
        log = login.LoginWindow()
        log.add_frame()

    def teacher_login(self):
        # destroy current window
        self.win.destroy()

        #open the new window
        tlog = teacherlogin.TeacherLoginWindow()
        tlog.add_frame()


if __name__ == "__main__":
    x = WelcomeWindow()
    x.add_frame()