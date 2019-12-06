"""
File Name: Tkinter_Practice.py
Name: Matt Robinson
Description: This file's sole purpose is to just get me familiar with Tkinter so I can potentially use
             it for a front end for the gpa calculator
"""
from tkinter import *


def test():
    buttons = int(input("How many buttons?"))
    m = Tk()
    m.title('GPA Calculator')
    m.wm_minsize(width=1000, height=500)
    for i in range(0, buttons):
        button = Button(m, text="Test", height=1, width=25, command=lambda: button_function("test", m))
        button.place(x=0, y=i*100)
    m.mainloop()


def button_function(text,m):
    print(text)
    button = Button(m, text="who knows", height=1, width=25, command=lambda: print("blah"))
    button.place(relx=.5, rely=.5)


if __name__ == '__main__':
    test()
