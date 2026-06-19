from tkinter import *
from tkinter import ttk
import time


msg = None
i = -1

L = ["Hello-1", "Hello-10", "Hello-100"]

def change_button_handler():
    global i
    i = (i+1) % len(L)
    msg.set(L[i])
    s = msg.get()
    print(s)

def main():
    global msg

    root_window = Tk()
    root_window.title("Feet to meter conversion")
    root_window.geometry('200x250')
    
    msg = StringVar()
    LB = ttk.Label(root_window)
    LB.configure(textvariable= msg)
    msg.set("START")
    LB.grid(row=1, column=1)

    B = Button(root_window)
    B.configure(text="Change", command=change_button_handler)
    B.grid(row=1, column=0)

    root_window.mainloop()

main()