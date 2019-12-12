"""
File Name: Tkinter_Practice.py
Name: Matt Robinson
Description: This file's sole purpose is to just get me familiar with Tkinter so I can potentially use
             it for a front end for the gpa calculator
"""
from tkinter import *
'''
Useful Links:

https://stackoverflow.com/questions/36575890/how-to-set-a-tkinter-window-to-a-constant-size
https://www.geeksforgeeks.org/python-gui-tkinter/
'''

credit_hours = [0,1,2,3,4,5]
grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "E", "F"]


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


# Following link may solve issue
# https://stackoverflow.com/questions/8369560/finding-widgets-on-a-grid-tkinter-module
def pretty_layout():
    m = Tk()
    m.title('GPA Calculator')
    m.wm_minsize(width=1000, height=500)
    title_bar1 = Label(m, text="Class Name", width=24, font=("Times New Roman", 30)).grid(row=0, column=0)
    title_bar2 = Label(m, text="Credit Hours", width=25, font=("Times New Roman", 30)).grid(row=0, column=1)
    title_bar3 = Label(m, text="Grade", width=25, font=("Times New Roman", 30)).grid(row=0, column=2)
    for i in range(1, 6):
        e = Entry(m).grid(row=i, column=0)
        var = StringVar(m)
        var.set("-")
        var2 = StringVar(m)
        var2.set("-")
        o = OptionMenu(m, var, *credit_hours).grid(row=i, column=1)
        o2 = OptionMenu(m, var2, *grades).grid(row=i, column=2)
    button = Button(m, text="Calculate GPA", command=lambda: calculate_gpa(m)).grid(row=6, column=1)
    m.mainloop()


def calculate_gpa(m):
    """
    x = m.grid_size()[0]
    y = m.grid_size()[1]
    print("X: " + str(x))
    print("Y: " + str(y))
    """
    get_values(m)


def get_values(m):
    for child in m.children.values():
        info = child.grid_info()
        if 0 < info['row'] < 6 and info['column'] > 0:
            print(child['text'])


if __name__ == '__main__':
    pretty_layout()
