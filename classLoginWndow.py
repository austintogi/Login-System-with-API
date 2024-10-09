import json
import tkinter as tk
from tkinter import RAISED, Button, Entry, Label, StringVar, Tk, ttk
from classDetailsWindow import DetailsWindow
import user_model as um
import requests 

class LoginWindow:
    def __init__(self):
        self.app = Tk()
        self.app.title("Login")
        self.app.resizable(False, False)
        self.app.geometry("370x150")
        self.varForError=StringVar()
        self.label=Label(self.app, text='USERNAME',font=("Courier 20 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=0)
        self.label=Label(self.app, text='PASSWORD',font=("Courier 20 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=30)
        self.label=Label( self.app, textvariable=self.varForError,font=("Courier 14 "),bg="black",fg="red", relief=RAISED).place(x=100,y=115)
    
        self.entry= Entry(self.app, width= 16)
        self.entry.focus_set()
        self.entry.pack()
        
        self.entryPassword= Entry(self.app, width= 16)
        self.entryPassword.focus_set()
        self.entryPassword.pack()
        
        self.login = Button(self.app, text="Login",pady=5, padx=30, command=lambda: [onLoginNow(username=self.entry.get(),Password=self.entryPassword.get(),varForError=self.varForError,loginWindow=self)])
        self.login.place(x=100,y=60)
    def run(self):
        self.app.mainloop()
    def exit(self):
        self.app.destroy()
  
def onLoginNow(username,Password,varForError,loginWindow:LoginWindow):
    if len(username)>=4 and len(username)<=8:
        varForError.set('')
        print("Valid Username")
        contains_uppercase = any(char.isupper() for char in Password)
        if contains_uppercase:
            varForError.set('')
            print("Valid Password")
            _req=None
            url="https://jsonplaceholder.typicode.com/users"
            response=requests.get(url)
            print(response.status_code)
            if response.status_code==200:
                x=response.content
                _req=json.loads(x)
                print("###SuccessRequest ==>") 
                remoteUsers=[]
                if _req!=None:  
                    for data in _req:
                        user = um.User.from_dict(data)
                        remoteUsers.append(user)
                    selected=None;
                    for user in remoteUsers:
                            if user.username == username:
                                selected = user
                            else:
                                varForError.set("Register First")
                    detail = DetailsWindow(loggedUser=selected)
                    loginWindow.exit()
                    detail.run()
        else:
            varForError.set("Must include 1 Upper")
            print("Invalid Password")
    else:
        varForError.set("Mini:4, Max:8")
        print("Usename Invalid")