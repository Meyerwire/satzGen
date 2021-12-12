import tkinter as tk
import tkinter.messagebox as tkm
import json
import helperClass
import json

with open('wordlist.json','r') as mylist:
    wList = mylist.read()

wordlist_json = json.loads(wList)

window = tk.Tk()
window.title ("Zufällige Sätze")
window.geometry("300x150")
window.resizable(False,False)

GoButton = tk.Button(window,width=10,text = "Go" ,  command =lambda: helperClass.GenSent(wordlist_json,tkm))
GoButton.pack()

window.mainloop()