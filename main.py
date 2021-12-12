import tkinter as tk
from random import randint

window = tk.Tk()

window.title = "Zufällige Sätze"

window.geometry("600x400")
newlabel = tk.Label(text = "Satz Generator")

newlabel.grid(column=0,row=0)
window.mainloop()