import json
import tkinter as tk
from tkinter import RAISED, Entry, StringVar, ttk
import user_model as um

import requests


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('370x150')
        self.title('User LogIn')

        ttk.Button(self,
                text='Close',
                command=self.destroy).pack(expand=True)


class App(tk.Tk):
    
    def onLoginClick(self,entry,entryPassword,varForError):
        string=entry.get()
        stringPassword=entryPassword.get()
        if len(string)>=4 and len(string)<=8:
            print("Usename valid")
            varForError.set('')
            contains_uppercase = any(char.isupper() for char in stringPassword)
            if contains_uppercase:
                varForError.set('')
                print("Valid Password")
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
                                if user.username == string:
                                    print("$$$$$$$")
                                        # newWindow=secondWindowLabels(loggedUser=user)
                                else:
                                    varForError.set("Register First")
                    else:
                        print('###BadRequest ==>')
                else:
                    varForError.set("Must include 1 Upper")
                    print("Invalid Password")
        else:
            varForError.set("Mini:4, Max:8")
            print("Usename Invalid")   
    def __init__(self):
        super().__init__()

        self.geometry('370x150')
        self.title('User LogIn')
        varForError=StringVar()
        entry= Entry(self, width= 16)
        entry.focus_set()
        entry.pack()
        #for 2nd box, for password
        entryPassword= Entry(self, width= 16)
        entryPassword.focus_set()
        entryPassword.pack()        
            # place a button on the root window
        tk.Label( self, textvariable=varForError,font=("Courier 14 "),bg="black",fg="red").place(x=100,y=115)
        tk.Label(self, text='USERNAME',font=("Courier 20 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=0)
        tk.Label(self, text='PASSWORD',font=("Courier 20 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=30)
        # ttk.Button(self, text='REGISTER',command=onRegisterClick, width=0.5).place(x=100,y=85)
        ttk.Button(self, text='LOGIN',command=self.onLoginClick(entry,entryPassword,varForError), width=0.5).place(x=100,y=60)

    # def open_window(self):
    #     window = Window(self)
    #     window.grab_set()

if __name__ == "__main__":
    app = App()
    app.mainloop()