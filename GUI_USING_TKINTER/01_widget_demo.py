import tkinter
import tkinter.ttk
import sys

def terminate():
    print("exiting the app..")
    sys.exit(0)


root_window = tkinter.Tk()
root_window.geometry('250x200')
root_window.title("Test Window")

master_frame = tkinter.ttk.Frame(root_window, padding="3 3 12 12")
master_frame.grid(row = 0, column=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))

B = tkinter.Button()
B.configure(text="EXIT BUTTON", command=terminate)
B.grid(row=0, column=0)

root_window.mainloop()

#Language + Logic + Domain

#Language: Syntax, Semantics, Memory Management, Type System Analysis
#Logic:     DSA and its application
#Domain:    Theory Knowledge, Domain Specofoc packages