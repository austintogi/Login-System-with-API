import json
from functions import checkWithJsonMapping
from showingDetails import secondWindowLabels
import user_model as um
import tkinter as tk
from tkinter import DISABLED, END, LEFT, RAISED, RIGHT, Entry, Label, StringVar, Text, Tk, Toplevel, ttk
from tkinter.messagebox import showinfo
import requests

root = tk.Tk()
root.geometry('370x150')
root.resizable(False, False)
root.title('LOGIN')

varForError=StringVar()

tk.Label(root, text='USERNAME',font=("Courier 20 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=0)
tk.Label(root, text='PASSWORD',font=("Courier 20 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=30)

entry= Entry(root, width= 16)
entry.focus_set()
entry.pack()

#for 2nd box for password
entryPassword= Entry(root, width= 16)
entryPassword.focus_set()
entryPassword.pack()
def quitForFirstWindow():
    global root
    root.destroy()
def onLoginClick():
    global entry
    global entryPassword
    global root
    username= entry.get()
    Password=entryPassword.get()
    if len(username)>=4 and len(username)<=8:
        varForError.set('')
        contains_uppercase = any(char.isupper() for char in Password)
        if contains_uppercase:
            varForError.set('')
            print("Valid Password")
            checkWithJsonMapping(username=username)
            root.destroy()
        else:
            varForError.set("Must include 1 Upper")
            print("Invalid Password")
    else:
        varForError.set("Mini:4, Max:8")
        print("Usename Invalid")
def onRegisterClick():
    root.destroy()
    import registrationPage
tk.Label( root, textvariable=varForError,font=("Courier 14 "),bg="black",fg="red", relief=RAISED).place(x=100,y=115)
#to create a button for login and register
ttk.Button(root, text='REGISTER',command=onRegisterClick, width=0.5).place(x=100,y=85)
ttk.Button(root, text='LOGIN',command=lambda: [onLoginClick()], width=0.5).place(x=100,y=60)
root.mainloop()