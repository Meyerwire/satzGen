from random import randint
from tkinter import OptionMenu

def GenSent(wList,tkm):
    satz = ""
    for val in wList:
        satz += wList[val][str(randint(1,len(wList[val])))]
        satz +=" "
    satz.strip
    satz+="."
    tkm.showinfo("Satz",satz)

def AddWord(tk,master_window):
    print("test")
    #alert init
    AddAlert = tk.Toplevel(master_window)
    AddAlert.title("Add")
    AddAlert.geometry("150x150")
    AddAlert.resizable(False,False)
    inputField = tk.Canvas(AddAlert).pack()
    OPTIONS = ["one","two","three"]
    val = tk.StringVar(master_window)
    val.set(OPTIONS[0])
    optsMenu = OptionMenu(master_window,val,"1","2").pack()