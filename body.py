import json
import post_model as pm
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import showinfo
import requests

class Body:
    def __init__(self,loggedUser:pm.Root):
        self.app = Tk()
        self.app.title("Login with Python")
        self.app.resizable(False, False)
        self.app.geometry("300x250")
        self.varForBody.set(str(loggedUser.body))
        self.label=Label(self.app, text=self.varForBody.get(),font=("Courier 12 bold"),relief=RAISED).place(x=60,y=0)
    def run(self):
        self.app.mainloop()
    def exit(self):
        self.app.destroy()
def bodyView(listForJson):
    root = tk.Tk()
    root.title("Body of the title")
    root.geometry("370x150")
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )
    var = tk.Variable(value=listForJson)
    mylist = Listbox(root,listvariable=var,height=100,selectmode=tk.EXTENDED, yscrollcommand = scrollbar.set )
    for item in listForJson:
        mylist.insert(END, str(item))
    mylist.pack(expand=True,fill = BOTH)
    mylist.activate(0)
    scrollbar.config( command = mylist.yview)
    root.mainloop()
def showTitle():
    _req=None
    url="https://jsonplaceholder.typicode.com/posts"
    response=requests.get(url)
    print(response.status_code)
    if response.status_code==200:
        x=response.content
        _req=json.loads(x)          
        list=[]
        if _req!=None:
            for data in _req:      
                p = Body()
                p.mapFromJson(data)
                list.append(p)
            for destring in list:
                print(destring)
            bodyView(listForJson=list)