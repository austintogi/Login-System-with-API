import json
import user_model as um
import tkinter as tk
from tkinter import DISABLED, END, LEFT, RAISED, RIGHT, Entry, Label, StringVar, Text, Tk, Toplevel, ttk
from tkinter.messagebox import showinfo
import requests
# 1st window for logging in: First Root window
root = tk.Tk()
root.geometry('370x150')
root.resizable(False, False)
root.title('LOGIN')
rootThird=Tk()
rootThird.geometry("1x1")

#for closing 1st window
def quitForFirstWindow():
    root.destroy()
    print('1st Tkinter window closed ✅')
def quitForSecondWindow():
    rootSecond.destroy()
    print('2nd Tkinter window closed ✅')
def quitForThirdWindow():
    rootThird.destroy()
    print('3rd Tkinter window closed ✅')

#for creating 2nd window
rootSecond=Tk()
rootSecond.geometry("1x1")

#variable for displaying error
varForError=StringVar()

#to create username button and disable it
tk.Label(root, text='USERNAME',font=("Courier 20 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=0)
tk.Label(root, text='PASSWORD',font=("Courier 20 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=30)

entry= Entry(root, width= 16)
entry.focus_set()
entry.pack()

#for 2nd box, for password
entryPassword= Entry(root, width= 16)
entryPassword.focus_set()
entryPassword.pack()

#FUNCTIONS
######################################################################################################################################################################################################
# #function to open 2nd window
def secondWindowLabels(loggedUser:um.User):   
    #for creating window
    rootSecond=Tk()
    rootSecond.geometry('370x150')
    rootSecond.resizable(False, False)
    rootSecond.title('SHOWING YOR DETAILS')
    #Creating var to set data in respective fields
    varForName=StringVar()
    varForMail=StringVar()
    varForAddress=StringVar()
    varForStreet=StringVar()
    varForSuite=StringVar()
    varForCity=StringVar()
    varForZipcode=StringVar()
    varForName.set(str(loggedUser.name))
    varForMail.set(str(loggedUser.email))
    varForStreet.set(str(loggedUser.address.street))
    # varForAddress.set(str(loggedUser.address))
    varForCity.set(str(loggedUser.address.city))
    varForSuite.set(str(loggedUser.address.suite))
    varForZipcode.set(str(loggedUser.address.zipcode))
    # to Create labels for name,mail id and password
    tk.Label(rootSecond, text='NAME : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=0)
    tk.Label(rootSecond, text='EMAIL ID : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=30)
    tk.Label(rootSecond, text='ADDRESS : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=60)
    #to create labels that display their details with json
    tk.Label(rootSecond, textvariable=varForName,font=("Courier 12 bold"),relief=RAISED).place(x=60,y=0)
    tk.Label(rootSecond, textvariable=varForMail,font=("Courier 12 bold"),relief=RAISED).place(x=88,y=30)
    # tk.Label(rootSecond, textvariable=varForAddress,font=("Courier 12 bold"),relief=RAISED).place(x=81,y=60)
    #to create labels that display street, suite, city, zipcode
    tk.Label(rootSecond, text="STREET : ",font=("Courier 12 bold"),bg="black",fg="red",relief=RAISED).place(x=25,y=88)
    tk.Label(rootSecond, text="SUITE : ",font=("Courier 12 bold"),bg="black",fg="red",relief=RAISED).place(x=25,y=113)
    tk.Label(rootSecond, text="CITY : ",font=("Courier 11 bold"),bg="black",fg="red",relief=RAISED).place(x=185,y=88)
    tk.Label(rootSecond, text="ZIPCODE : ",font=("Courier 11 bold"),bg="black",fg="red",relief=RAISED).place(x=185,y=113)
    #to create labels that display street, suite, city, zipcode
    tk.Label(rootSecond, textvariable=varForStreet,font=("Courier 12 bold"),relief=RAISED).place(x=97,y=88)
    tk.Label(rootSecond, textvariable=varForSuite,font=("Courier 12 bold"),relief=RAISED).place(x=91,y=113)
    tk.Label(rootSecond, textvariable=varForCity,font=("Courier 12 bold"),relief=RAISED).place(x=245,y=88)
    tk.Label(rootSecond, textvariable=varForZipcode,font=("Courier 12 bold"),relief=RAISED).place(x=264,y=113)
    rootSecond.mainloop()
# #function for registering
def onRegisterClick():
    #for creating window
    rootThird=Tk()
    rootThird.geometry('370x150')
    rootThird.resizable(False, False)
    rootThird.title('REGISTERING')
    #Creating var to set data in respective fields
    varForUsernameRegister=StringVar()
    varForRegisterError=StringVar()
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
    quitForFirstWindow()
    # global entry
    # global entryPassword
    userName=entry.get()
    passWord=entryPassword.get()
    confirmPassWord=entryConfirmPassword.get()
    # close=quitForFirstWindow()
    if len(userName)>=4 and len(userName)<=8:   
        varForRegisterError.set('')
        print("Registering Successfully")
        contains_uppercase = any(char.isupper() for char in passWord)  
        if contains_uppercase:
            varForRegisterError.set('')
            print("Valid Password")
            if passWord==confirmPassWord:
                varForRegisterError.set('')
                varForRegisterError.set("REGISTERED SUCCESSFULLY")
            else:
                varForRegisterError.set('')
                varForRegisterError.set("Pass and confirm pass should be same")
        else:
            varForRegisterError.set('')
            varForRegisterError.set("Must include 1 Upper")
            print("Invalid Password")
    else:
        varForRegisterError.set("Mini:4, Max:8")
        print("Registering Failed")

    tk.Label( rootThird, textvariable=varForRegisterError,font=("Courier 14 "),bg="black",fg="red", relief=RAISED).place(x=100,y=115)
    tk.Label( rootThird, textvariable=varForRegisterError,font=("Courier 14 "),bg="black",fg="red", relief=RAISED).place(x=100,y=115)
    tk.Label(rootThird, text='USERNAME : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=0)
    tk.Label(rootThird, text='PASSWORD : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=30)
    tk.Label(rootThird, text='CONFIRM PASS : ',font=("Courier 12 bold"),bg="red",fg="black", relief=RAISED).place(x=0,y=60)
    ttk.Button(rootThird, text='REGISTER NOW',command=lambda: [onRegisterClick()], width=0.5).place(x=100,y=90)
    rootThird.mainloop()
# function for checking with json
def getResponse(url):
    _req=None
    response=requests.get(url)
    print(response.status_code)
    if response.status_code==200:
        x=response.content
        _req=json.loads(x)
        print("###SuccessRequest ==>") 
        # print(_req)
        # print("###################")
    else:
        print('###BadRequest ==>')
    return _req
#function for logging in
def onLoginClick():
    global entry
    global entryPassword
    string= entry.get()
    stringPassword=entryPassword.get()
    if len(string)>=4 and len(string)<=8:
        varForError.set('')
        for eachLetter in stringPassword:
            contains_uppercase = any(char.isupper() for char in stringPassword)
            if contains_uppercase:
                varForError.set('')
                print("Valid Password")
                rs=getResponse(url="https://jsonplaceholder.typicode.com/users")
                remoteUsers=[]
                if rs!=None:  
                    for data in rs:
                        user = um.User.from_dict(data)
                        remoteUsers.append(user)
                        for user in remoteUsers:
                            if user.username == string:
                                close=quitForFirstWindow()
                                newWindow=secondWindowLabels(loggedUser=user)
                            else:
                                registerWindow=onRegisterClick()
                                varForError.set("Register First")
            else:
                varForError.set("Must include 1 Upper")
                print("Invalid Password")
    else:
        varForError.set("Mini:4, Max:8")
        print("Usename Invalid")
#############################################################################################################################################################################################################################################################################################################################################################################################################################################################
#another label for error
tk.Label( root, textvariable=varForError,font=("Courier 14 "),bg="black",fg="red", relief=RAISED).place(x=100,y=115)
#to create a button for login and register
ttk.Button(root, text='REGISTER',command=onRegisterClick, width=0.5).place(x=100,y=85)
ttk.Button(root, text='LOGIN',command=lambda: [onLoginClick()], width=0.5).place(x=100,y=60)
quitForThirdWindow()
quitForSecondWindow()
root.mainloop()
#####################################################################################################################################################################################################################################################################################################################################