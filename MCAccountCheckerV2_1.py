from tkinter import *
import requests
import json
import base64
import webbrowser

def callback(url):
    webbrowser.open_new(url)

def myClick():
    response = requests.get("https://api.mojang.com/users/profiles/minecraft/"+e.get())
    x = response.json()
    userid = x["id"]
    name = x["name"]
    
    response2 = requests.get("https://sessionserver.mojang.com/session/minecraft/profile/"+userid)
    y = response2.json()['properties']
    p = []

    for d in y:
        val = d['value']
        p.append(val)

    base64_message = p[0]
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    split = message.split('"')
    skin = split[17]
    
    
    
    #printing
    myText = Label(root, text='ID: '+userid)
    myText.pack()
    myText1 = Label(root, text='Name: '+name)
    myText1.pack()
    link1 = Label(root, text="Skin", fg="blue", cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback(skin))

    if len(split) == 19:
        myText3 = Label(root, text='Cape: False')
        myText3.pack()
    elif len(split) > 19:
        myText4 = Label(root, text='Cape: True')
        myText4.pack()

root = Tk()
root.title('MC Account Checker v2.1')

myLabel = Label(root, text='Enter a username to look up')
myLabel.pack()

e = Entry(root, width=50)
e.pack()

myButton = Button(root, text='Enter', command=myClick)
myButton.pack()

root.mainloop()