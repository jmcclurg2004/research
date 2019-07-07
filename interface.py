#author: Jerry McClurg
#Version 1 7/6/2019
import sys
import os
from tkinter import *

window=Tk()

window.title("HTTP Header Analysis")
window.geometry('275x50')

def run():
    os.system('headers.py')

btn = Button(window, text="Click Here and Enter URL in Command Window", bg="black", fg="white",command=run)
btn.grid(column=0, row=0)

window.mainloop()
