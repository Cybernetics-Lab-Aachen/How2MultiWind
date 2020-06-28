from tkinter import *
from tkinter import messagebox

top = Tk()
def hello():
    messagebox.showinfo("information", "Information")

B1 = Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()