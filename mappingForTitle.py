import json
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter.messagebox import showinfo
import requests
from post_model import Post

from test import bodyView
from classTitleWindow import TitleWindow


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
                list.append(Post.from_dict(data))
            title=TitleWindow(varForlist=list)
            title.run()























# def listView(listForJson):
#     root = tk.Tk()
#     root.title("Showing posts")
#     root.geometry("400x200")
#     scrollbar = Scrollbar(root)
#     scrollbar.pack( side = RIGHT, fill = Y )
#     var = tk.Variable(value=listForJson)
#     mylist = Listbox(root,listvariable=var,height=100,selectmode=tk.EXTENDED, yscrollcommand = scrollbar.set )
#     for item in listForJson:
#         mylist.insert(END, str(item))
#     mylist.pack(expand=True,fill = BOTH )
#     mylist.activate(0)
#     mylist.bind('<Double-Button-1>', lambda:bodyView())
#     scrollbar.config( command = mylist.yview)
#     # bodyView(listForJson=listForJson)
#     # root.destroy()
#     root.mainloop()
    