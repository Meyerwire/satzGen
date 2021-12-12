import tkinter as tk
import tkinter.messagebox as tkm
import json
import helperClass
import json

with open('wordlist.json','r') as mylist:
    wList = mylist.read()

wordlist_json = json.loads(wList)



window = tk.Tk()

window.title = "Zufällige Sätze"
window.geometry("600x400")

newlabel = tk.Label(text = "Satz Generator")
newlabel.grid(column=0,row=0)

GoButton = tk.Button(window,text = "Go" ,  command = helperClass.GenSent(wordlist_json,tkm) )
GoButton.grid(column=100,row=100)



window.mainloop()