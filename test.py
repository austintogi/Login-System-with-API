import json
import post_model as pm
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import showinfo
import requests

class Body:
    def mapFromJson(self,obj):
        self.body=obj['body']
    def __str__(self):
        return f"{self.body}"
def bodyView(e):
    root = tk.Tk()
    root.title("Body of the Title")
    root.geometry("350x120")
    varForBody = StringVar()
    label=Label(root, textvariable=varForBody,font=("Courier 20 bold"),bg="red",fg="black")
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
                print("$$$$$$$$$$$$$$$$###############@@@@@@@@@@@@@@@@@@")
                varForBody.set(str(destring))
                print(destring)
    root.mainloop()