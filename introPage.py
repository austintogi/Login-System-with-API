from tkinter import *
from classLoginWndow import LoginWindow
from classRegistrationWindow import RegisterWindow
from classDetailsWindow import DetailsWindow
global mainWindow
global loginTk
global registerTk
class MainWindow:
    def __init__(self):
        self.app = Tk()
        self.app.title("Login with Python")
        self.app.geometry("300x250")
        self.label = Label(self.app, text='WELCOME',font=("Courier 20 bold"),bg="red",fg="black")
        self.label.place(x=95, y=40)
        self.login = Button(self.app, text="Login",pady=5, padx=30, command=login)
        self.login.place(x=100, y=100)
        self.register = Button(self.app, text="Register",pady=5, padx=20, command=register)
        self.register.place(x=100, y=150)
    def run(self):
        self.app.mainloop()
    def exit(self):
        self.app.destroy()
def login():
    mainWindow.exit()
    loginTk = LoginWindow()
    loginTk.run()
def register():
    mainWindow.exit()
    registerTk = RegisterWindow()
    registerTk.run()
mainWindow = MainWindow()
mainWindow.run()