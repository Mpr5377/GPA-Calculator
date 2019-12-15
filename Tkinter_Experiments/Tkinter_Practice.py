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

credit_hours = [1, 2, 3, 4, 5]
grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "E", "F"]
grade_dict = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1,
    "E": 0,
    "F": 0
}


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
    button = Button(m, text="Add Class", command=lambda: add_class(m)).grid(row=6, column=0)
    button2 = Button(m, text="Calculate GPA", command=lambda: get_values(m)).grid(row=6, column=2)
    gpa_label = Label(m, text="N/A", width=25, font=("Times New Roman", 30)).grid(row=7, column=1)
    m.mainloop()


def add_class(m):
    print(m.grid_size())
    y = int(m.grid_size()[1]) - 2
    blah = int(m.grid_size()[1])
    print("Y:", y, blah)
    m.grid_slaves(y, 2)[0].destroy()
    m.grid_slaves(y, 0)[0].destroy()
    e = Entry(m).grid(row=y, column=0)
    var = StringVar(m)
    var.set("-")
    var2 = StringVar(m)
    var2.set("-")
    o = OptionMenu(m, var, *credit_hours).grid(row=y-1, column=1)
    o2 = OptionMenu(m, var2, *grades).grid(row=y-1, column=2)
    button = Button(m, text="Add Class", command=lambda: add_class(m)).grid(row=y+2, column=0)
    button2 = Button(m, text="Calculate GPA", command=lambda: get_values(m)).grid(row=y+2, column=2)


def calculate_gpa(grades_list,m):
    y = int(m.grid_size()[1]) - 1
    m.grid_slaves(y, 1)[0].destroy()
    gpa_total = 0
    hour_total = 0
    for grade in grades_list:
        hours = grade[0]
        class_gpa = grade[1]
        if hours == '-' or class_gpa == '-':
            pass
        else:
            hours = float(hours)
            class_gpa = float(grade_dict.get(class_gpa))
            gpa_total += hours * class_gpa
            hour_total += hours
    if hour_total is 0:
        gpa_total = 0
    else:
        gpa_total = round(gpa_total/hour_total, 2)
    gpa_label = Label(m, text=gpa_total, width=25, font=("Times New Roman", 30)).grid(row=y, column=1)


def get_values(m):
    """
    x = m.grid_size()[0]
    y = m.grid_size()[1]
    print("X: " + str(x))
    print("Y: " + str(y))
    """
    grades_list = []
    prev_child = None
    for child in m.children.values():
        info = child.grid_info()
        current_row = info['row']
        current_col = info['column']
        if 0 < int(current_row) < 6 and int(current_col) > 0:
            if prev_child is None:
                pass
            elif prev_child.grid_info()['row'] == current_row:
                grade = (prev_child['text'], child['text'])
                grades_list.append(grade)
            prev_child = child
    calculate_gpa(grades_list,m)


if __name__ == '__main__':
    pretty_layout()
