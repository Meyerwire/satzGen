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
master_window = tk.Tk()
master_window.title ("Zufällige Sätze")
master_window.geometry("300x150")
master_window.resizable(False,False)


#buttons inout fields etc
GoButton = tk.Button(master_window,width=10,text = "Go" ,  command =lambda: helperClass.GenSent(wordlist_json,tkm)).pack()
AddButton = tk.Button(master_window,width=10,text="Add",command=lambda: helperClass.AddWord(tk,master_window) ).pack()

master_window.mainloop()