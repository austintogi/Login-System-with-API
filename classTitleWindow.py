from ast import List
import json

from pyparsing import Any
from showPosts import ShowPostsWindow
from test import bodyView
import user_model as um
import post_model as pm
import tkinter as tk
from tkinter import ANCHOR, BOTH, DISABLED, END, LEFT, RAISED, RIGHT, Y, Button, Entry, Label, Listbox, Scrollbar, StringVar, Text, Tk, Toplevel, Variable, ttk
from tkinter.messagebox import showinfo
import requests

class TitleWindow:
    def __init__(self,varForlist:List):
        self.app = Tk()
        self.app.title("Showing all titles")
        self.app.resizable(False, False)
        self.app.geometry("400x200")
        self.scrollbar = Scrollbar(self.app)
        self.scrollbar.pack( side = RIGHT, fill = Y )
        self.titles  = []
        for x in varForlist:
          self.titles.append(x.title)
        self.var = Variable(value=self.titles)
        self.mylist = Listbox(self.app,height=100,listvariable=self.var, yscrollcommand = self.scrollbar.set )
        self.mylist.bind('<Double-Button-1>',func=lambda a:[closeTitleWindow(titleWindow=self,selected=self.mylist.get(ANCHOR),varForlist=varForlist),openDetailWindow(a)])
        self.mylist.pack(expand=True,fill = BOTH )
    def run(self):
        self.app.mainloop()
    def exit(self):
        self.app.destroy()

def closeTitleWindow(titleWindow:TitleWindow,selected:Any,varForlist:List):
    post=None;
    for x in varForlist:
      if(x.title ==selected):
         post=x
    if(post!=None):
        titleWindow.exit()
        detail = PostDetailWindow(post=post)
        detail.run()

def openDetailWindow(a):
    print('Butn Click')


class PostDetailWindow:
    def __init__(self,post:pm.Post):
        self.app = Tk()
        self.app.title("Post Detail")
        self.app.geometry("460x150")
        self.label = Label(self.app, text=post.body,font=("Courier 14 bold"),bg="red",fg="black")
        self.label.place(x=0, y=0)
    def run(self):
        self.app.mainloop()
    def exit(self):
        self.app.destroy()