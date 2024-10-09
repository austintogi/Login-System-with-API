import json
# from loginPage import root
from showingDetails import secondWindowLabels
import user_model as um
import tkinter as tk
from tkinter import DISABLED, END, LEFT, RAISED, RIGHT, Entry, Label, StringVar, Text, Tk, Toplevel, ttk
from tkinter.messagebox import showinfo
import requests

def quitForFirstWindow():
    global root
    root.destroy()
def checkWithJsonMapping(username):
    # global entry
    # global entryPassword
    # string= entry.get()
    varForError=StringVar()
    # rs=getResponse(url="https://jsonplaceholder.typicode.com/users")
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
            # user.mapFromJson(data)
                remoteUsers.append(user)
                for user in remoteUsers:
                    if user.username == username:
                        close=quitForFirstWindow()
                        print("$$$$$$$")
                        newWindow=secondWindowLabels(loggedUser=user)
                    else:
                        varForError.set("Register First")
    else:
        print('###BadRequest ==>')
