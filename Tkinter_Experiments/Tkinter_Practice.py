"""
File Name: Tkinter_Practice.py
Name: Matt Robinson
Description: This file's sole purpose is to just get me familiar with Tkinter so I can potentially use
             it for a front end for the gpa calculator
"""
from tkinter import *


def test():
    m = Tk()
    m.title('GPA Calculator')
    m.wm_minsize(width=1000,height=500)
    m.mainloop()


if __name__ == '__main__':
    test()
