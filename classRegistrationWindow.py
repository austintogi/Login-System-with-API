import json
import tkinter as tk
from tkinter import DISABLED, END, LEFT, RAISED, RIGHT, Button, Entry, Label, StringVar, Text, Tk, Toplevel, ttk
from tkinter.messagebox import showinfo
import requests


class RegisterWindow:
    def __init__(self):
        self.app = Tk()
        self.app.title("Register")
        self.app.resizable(False, False)
        self.app.geometry("370x200")
        self.varForError=StringVar()
        
        self.label=Label( self.app, textvariable=self.varForError,font=("Courier 14 "),bg="black",fg="red", relief=RAISED).place(x=100,y=150)
        
        
        self.entryRUsername= Entry(self.app, width= 12)
        self.entryRUsername.focus_set()
        self.entryRUsername.pack()
        self.entryRPassword= Entry(self.app, width= 12)
        self.entryRPassword.focus_set()
        self.entryRPassword.pack()
        self.entryRConfirmPassword= Entry(self.app, width= 12)
        self.entryRConfirmPassword.focus_set()
        self.entryRConfirmPassword.pack()
        self.label=Label(self.app, text='USERNAME : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=0)
        self.label=Label(self.app, text='PASSWORD : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=30)
        self.label=Label(self.app, text='CONFIRM PASS : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=60)
        self.registerNow=Button(
            self.app, 
            text='REGISTER NOW',
            command=lambda: [onRegisterNow(entryRUsername=self.entryRUsername.get(),entryRPassword=self.entryRPassword.get(),entryRConfirmPassword=self.entryRConfirmPassword.get(),varForRegisterError=self.varForError)]
            )
        self.registerNow.place(x=100,y=90)
        
    def run(self):
        self.app.mainloop()
    def exit(self):
        self.app.destroy()
        

def postResponse(data):
	url = 'https://jsonplaceholder.typicode.com/users'
	response = requests.post(url, data=json.dumps(data))
	json_data = response.json()
	print(response.status_code)
	print(json_data)
def onRegisterNow(entryRUsername,entryRPassword,entryRConfirmPassword,varForRegisterError):
    username=entryRUsername
    password=entryRPassword
    confirmPassword=entryRConfirmPassword
    if len(username)>=4 and len(username)<=8:
        varForRegisterError.set('')
        contains_uppercase = any(char.isupper() for char in password)
        if contains_uppercase:
            varForRegisterError.set('')
            if password==confirmPassword:
                varForRegisterError.set('')
                print("Valid Password")
                dataForRegister = {"username": entryRUsername.get(),"email": entryRConfirmPassword.get()}
                updateJson=postResponse(data=dataForRegister)
            else:
                varForRegisterError.set("Pass and Confirm pass should match")
        else:
            varForRegisterError.set("Must include 1 Upper")
            print("Invalid Password")
    else:
        varForRegisterError.set("Mini:4, Max:8")
        print("Usename Invalid")








































# def checkForLength(string):
#     # global entry
#     # global entryPassword
#     # string= entry.get()
#     varForError.set('')
#     if len(string)>=4 and len(string)<=8:
#         varForError.set('')
#         print("successfully")
#     else:
#         varForError.set("Mini:4, Max:8")
#         print("Usename Invalid")
# def checkForUpperCase(stringPassword):
#     # global entry
#     # global entryPassword
#     # stringPassword=entryPassword.get()
#     contains_uppercase = any(char.isupper() for char in stringPassword)
#     if contains_uppercase:
#         varForError.set('')
#         dataForRegister = {"username": entryRUsername.get(),"email": entryRConfirmPassword.get()}
#         updateJson=postResponse(data=dataForRegister)
#         print("Valid Password")
#     else:
#         varForError.set("Must include 1 Upper")
#         print("Invalid Password")
        
    #Creating var to set data in respective fields
# def onRegisterNow(entryRUsername,entryRConfirmPassword):
#     checkForLength(string=entryRUsername.get())
#     checkForUpperCase(stringPassword=entryRConfirmPassword.get())
#     # dataForRegister = {"username": entryRUsername.get(),"email": entryRConfirmPassword.get()}
#     # updateJson=postResponse(data=dataForRegister)
#     print("SUCCESSFULLY")



# checkForLength(string=entryRUsername.get())
# checkForUpperCase(stringPassword=entryRConfirmPassword.get())