import db
from tkinter import *
import tkinter as tk

class addNewStudent:

    def __init__(self, username):
        self.win = Tk()
        self.username = username
        self.canvas = Canvas(self.win, width=600, height=500, bg='lavender')
        self.win.config(bg = "lavender")
        #self.canvas.pack(expand=YES, fill=BOTH)

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
        self.win.title("MAIN MENU | QUIZU! | ADMINISTRATOR")

    def startAddNewStudent(self):

        label1 = tk.Label(self.win, text = "Add Student",
                         font=("Arial", 15), width=30)
        label1.config(bg="lavender")
        label1.grid(row=1, column=1, columnspan=4)

        #name
        label2 = tk.Label(self.win, text="Name: ", width=10)
        label2.config(bg = "lavender")
        label2.grid(row=3, column=1)

        text1 = tk.Text(self.win, height= 1, width=10, bg="white")
        text1.grid(row=3, column=2)

        #age
        label3 = tk.Label(self.win, text = "Age: ", width=10)
        label3.config(bg="lavender")
        label3.grid(row=4, column=1)

        text2 = tk.Text(self.win, height=1, width=10, bg="white")
        text2.grid(row=4, column=2)

        #subject
        label4 = tk.Label(self.win, text="Subject: ", width=10)
        label4.config(bg="lavender")
        label4.grid(row=5, column=1)

        text3 = tk.Text(self.win, height=1, width=10, bg="white")
        text3.grid(row=5, column=2)

        #username
        label5 = tk.Label(self.win, text="Username: ", width=10)
        label5.config(bg="lavender")
        label5.grid(row=6, column=1)

        text4 = tk.Text(self.win, height=1, width=10, bg="white")
        text4.grid(row=6, column=2)

        #password
        label6 = tk.Label(self.win, text="Password: ", width=10)
        label6.config(bg="lavender")
        label6.grid(row=7, column=1)

        text5 = tk.Text(self.win, height=1, width=10, bg="white")
        text5.grid(row=7, column=2)

        #class
        label7 = tk.Label(self.win, text="Class: ", width=10)
        label7.config(bg="lavender")
        label7.grid(row=8, column=1)

        options = StringVar(self.win)
        options.set("")

        option1 = OptionMenu(self.win, options, "CS1", "CS2", "ME1", "ME2", "EC1", "EC2")
        option1.grid(row=8, column=2)

        #gender
        radio_v = tk.StringVar()
        R1 = tk.Radiobutton(self.win, text="Male", variable=radio_v,value="Male")
        R1.config(bg = "lavender")
        R1.grid(row=9, column=1)

        R2 = tk.Radiobutton(self.win, text="Female", variable=radio_v,value="Female")
        R2.config(bg = "lavender")
        R2.grid(row=9, column=2)

        #output confirmation stuff
        my_str = tk.StringVar()
        label8 = tk.Label(self.win, textvariable=my_str, width=10)
        label8.config(bg="lavender")
        label8.grid(row=3, column=3)
        my_str.set("output")


        #insert begins
        addbtn = tk.Button(self.win, text="Add Student", width=10, command=(lambda: self.add_data(text1, options, text3, text4, text5, text2, radio_v, label8, my_str)))
        addbtn.config(bg="purple", fg="white")
        addbtn.grid(row=10, column=1)

    def add_data(self, name, myClass, subject, username, pw, age, gender, check, output):

        flag_validation = True
        my_name = name.get("1.0", END)
        my_class = myClass.get()
        my_gender = gender.get()
        my_subject = subject.get("1.0", END)
        my_age = age.get("1.0", END)
        my_username = username.get("1.0", END)
        my_password = pw.get("1.0", END)

        if(len(my_name) <2 or len(my_class) <2 or len(my_gender) <2 or len(my_subject) <2 or len(my_age) <2 or len(my_username) <2 or len(my_password) <2):
            flag_validation = False
            print("BBBBBBBBb")

        if(flag_validation):
            db.add_student(my_name, my_age, my_class, my_subject, my_password, my_username, my_gender)
        else:
            check.config(fg="black", bg="red")
            output.set("check inputs")

