import json
import post_model as pm
import tkinter as tk
from tkinter import BOTH, BOTTOM, DISABLED, END, LEFT, RAISED, RIGHT, X, Y, Button, Entry, Label, Listbox, Scrollbar, StringVar, Text, Tk, Toplevel, ttk
from tkinter.messagebox import showinfo
import requests

class ShowPostsWindow:
    def __init__(self,showPosts:pm.Post):
        self.app = Tk()
        self.app.title("Showing all posts")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(showPosts)
        # self.app.resizable(False, False)
        self.app.geometry("400x350")
        scrollbar = Scrollbar(self.app)
        scrollbar.pack( side = RIGHT, fill = Y )

        self.mylist = Listbox(self.app, yscrollcommand = scrollbar.set).pack( side = LEFT, fill = BOTH )
        # scrollbar.config( command = mylist.yview )
        # self.varForShowPosts=StringVar()
        # self.varForShowPosts.set(str(showPosts))
        # self.label=Label(self.app, textvariable=self.varForShowPosts,font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=0)
    def run(self):
        self.app.mainloop()
    def exit(self):
        self.app.destroy()

                                