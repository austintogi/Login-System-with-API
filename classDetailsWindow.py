import json
from showPosts import ShowPostsWindow
from mappingForTitle import showTitle
import user_model as um
import post_model as pm
import tkinter as tk
from tkinter import DISABLED, END, LEFT, RAISED, RIGHT, Button, Entry, Label, StringVar, Text, Tk, Toplevel, ttk
from tkinter.messagebox import showinfo
import requests

class DetailsWindow:
    def __init__(self,loggedUser:um.User):
        self.app = Tk()
        self.app.title("Login with Python")
        self.app.resizable(False, False)
        self.app.geometry("400x250")
        
        self.varForName=StringVar()
        self.varForMail=StringVar()
        self.varForStreet=StringVar()
        self.varForSuite=StringVar()
        self.varForCity=StringVar()
        self.varForZipcode=StringVar()
        
        self.varForName.set(str(loggedUser.name))
        self.varForMail.set(str(loggedUser.email))
        self.varForStreet.set(str(loggedUser.address.street))
        self.varForCity.set(str(loggedUser.address.city))
        self.varForSuite.set(str(loggedUser.address.suite))
        self.varForZipcode.set(str(loggedUser.address.zipcode))
        
        self.label=Label(self.app, text='NAME : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=0)
        self.label=Label(self.app, text='EMAIL ID : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=30)
        self.label=Label(self.app, text='ADDRESS : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=60)
        self.label=Label(self.app, text=self.varForName.get(),font=("Courier 12 bold"),relief=RAISED).place(x=60,y=0)
        self.label=Label(self.app, text=self.varForMail.get(),font=("Courier 12 bold"),relief=RAISED).place(x=88,y=30)
        self.label=Label(self.app, text="STREET : ",font=("Courier 12 bold"),bg="black",fg="red",relief=RAISED).place(x=25,y=88)
        self.label=Label(self.app, text="SUITE : ",font=("Courier 12 bold"),bg="black",fg="red",relief=RAISED).place(x=25,y=113)
        self.label=Label(self.app, text="CITY : ",font=("Courier 11 bold"),bg="black",fg="red",relief=RAISED).place(x=185,y=88)
        self.label=Label(self.app, text="ZIPCODE : ",font=("Courier 11 bold"),bg="black",fg="red",relief=RAISED).place(x=185,y=113)
        self.label=Label(self.app, text=self.varForStreet.get(),font=("Courier 12 bold"),relief=RAISED).place(x=97,y=88)
        self.label=Label(self.app, text=self.varForSuite.get(),font=("Courier 12 bold"),relief=RAISED).place(x=91,y=113)
        self.label=Label(self.app, text=self.varForCity.get(),font=("Courier 12 bold"),relief=RAISED).place(x=245,y=88)
        self.label=Label(self.app, text=self.varForZipcode.get(),font=("Courier 12 bold"),relief=RAISED).place(x=264,y=113)
        self.show=Button(self.app, text="Show",pady=5, padx=30, command=lambda: [onShowClick(detailsWindow=self)]).place(x=50,y=150)
        
    def run(self):
        self.app.mainloop()
    def exit(self):
        self.app.destroy()
def onShowClick(detailsWindow:DetailsWindow):
            detailsWindow.exit()
            showTitle()
                    
                        