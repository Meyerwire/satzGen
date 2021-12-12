import tkinter as tk
import tkinter.messagebox as tkm
import json
import helperClass
import json

#JSON file lesen
with open('wordlist.json','r') as mylist:
    wList = mylist.read()
#assoziatives array aus JSON file kreieren
wordlist_json = json.loads(wList)

#fenster initaliesieren
window = tk.Tk()
window.title ("Zufällige Sätze")
window.geometry("300x150")
window.resizable(False,False)
#alert init
AddAlert = tk.Tk()
AddAlert.title("Add")
AddAlert.geometry("150x150")
AddAlert.resizable(False,False)

#buttons inout fields etc
GoButton = tk.Button(window,width=10,text = "Go" ,  command =lambda: helperClass.GenSent(wordlist_json,tkm)).pack()
AddButton = tk.Button(window,width=10,text="Add",command=helperClass.AddWord ).pack()
inputField = tk.Canvas(AddAlert)

window.mainloop()