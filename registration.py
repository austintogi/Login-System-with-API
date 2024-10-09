# import loginPage
# import functions as fun
import json
import tkinter as tk
from tkinter import DISABLED, END, LEFT, RAISED, RIGHT, Entry, Label, StringVar, Text, Tk, Toplevel, ttk
from tkinter.messagebox import showinfo
import requests

#for creating window

rootThird=Tk()
rootThird.geometry('370x150')
rootThird.resizable(False, False)
rootThird.title('REGISTERING')

    #Creating var to set data in respective fields
varForUsernameRegister=StringVar()
varForPassword=StringVar()
varForConfirmPassword=StringVar()
entryUsernameForRegister= Entry(rootThird, width= 12)

entry= Entry(rootThird, width= 12)
entry.focus_set()
entry.pack()
#for 2nd box for password
entryPassword= Entry(rootThird, width= 12)
entryPassword.focus_set()
entryPassword.pack()

entryConfirmPassword= Entry(rootThird, width= 12)
entryConfirmPassword.focus_set()
entryConfirmPassword.pack()

varForError=StringVar()
def checkForLength(string):
    # global entry
    # global entryPassword
    # string= entry.get()
    varForError.set('')
    if len(string)>=4 and len(string)<=8:
        varForError.set('')
        print("successfully")
    else:
        varForError.set("Mini:4, Max:8")
        print("Usename Invalid")
def checkForUpperCase(stringPassword):
    # global entry
    # global entryPassword
    # stringPassword=entryPassword.get()
    contains_uppercase = any(char.isupper() for char in stringPassword)
    if contains_uppercase:
        varForError.set('')
        print("Valid Password")
    else:
        varForError.set("Must include 1 Upper")
        print("Invalid Password")
def onRegisterClick():
    #for creating window
    rootThird=Tk()
    rootThird.geometry('370x150')
    rootThird.resizable(False, False)
    rootThird.title('REGISTERING')
    varForRegisterError=StringVar()
    entryRUsername= Entry(rootThird, width= 12)
    entryRUsername.focus_set()
    entryRUsername.pack()
    entryRPassword= Entry(rootThird, width= 12)
    entryRPassword.focus_set()
    entryRPassword.pack()
    entryRConfirmPassword= Entry(rootThird, width= 12)
    entryRConfirmPassword.focus_set()
    entryRConfirmPassword.pack()
    #Creating var to set data in respective fields
    tk.Label( rootThird, textvariable=varForRegisterError,font=("Courier 14 "),bg="black",fg="red", relief=RAISED).place(x=100,y=115)
    tk.Label( rootThird, textvariable=varForRegisterError,font=("Courier 14 "),bg="black",fg="red", relief=RAISED).place(x=100,y=115)
    tk.Label(rootThird, text='USERNAME : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=0)
    tk.Label(rootThird, text='PASSWORD : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=30)
    tk.Label(rootThird, text='CONFIRM PASS : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=60)
    ttk.Button(rootThird, text='REGISTER NOW',command=lambda: [onRegisterNow(entryRUsername=entryRUsername,entryRConfirmPassword=entryRConfirmPassword)], width=0.5).place(x=100,y=90)
    checkForLength(string=entryRUsername.get())
    checkForUpperCase(stringPassword=entryRConfirmPassword.get())
def onRegisterNow(entryRUsername,entryRConfirmPassword):
    dataForRegister = {"username": entryRUsername.get(),"email": entryRConfirmPassword.get()}
    updateJson=postResponse(data=dataForRegister)
    print("SUCCESSFULLY")
varForRegisterError=StringVar()
def postResponse(data):
	url = 'https://jsonplaceholder.typicode.com/users'
	response = requests.post(url, data=json.dumps(data))
	json_data = response.json()
	print(response.status_code)
	print(json_data)
rootThird.mainloop()