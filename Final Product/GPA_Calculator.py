"""
File Name: GPA_Calculator.py
Name: Matt Robinson
Description: This is the final product of this little project. It is a fully functional GPA calculator, that you
             are able to add as many classes as you have, in order to find your gpa.
"""
from tkinter import *
credit_hours = ["-", 1, 2, 3, 4, 5]
grades = ["-", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "E", "F"]
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


def pretty_layout():
    """
    Function: pretty_layout()
    Description: This is the first function called in order to instantiate the interface. Defaults with 5 classes.
    :param: None
    :return: None
    """
    # Set up the Tkinter Window
    m = Tk()
    m.title('GPA Calculator')
    m.wm_minsize(width=1000, height=500)

    # Top bar with titles so the user understands each column
    title_bar1 = Label(m, text="Class Name", width=24, font=("Times New Roman", 30)).grid(row=0, column=0)
    title_bar2 = Label(m, text="Credit Hours", width=25, font=("Times New Roman", 30)).grid(row=0, column=1)
    title_bar3 = Label(m, text="Grade", width=25, font=("Times New Roman", 30)).grid(row=0, column=2)

    # Instantiating the drop down boxes for 5 classes
    for i in range(1, 6):
        e = Entry(m).grid(row=i, column=0)
        var = StringVar(m)
        var.set("-")
        var2 = StringVar(m)
        var2.set("-")
        o = OptionMenu(m, var, *credit_hours).grid(row=i, column=1)
        o2 = OptionMenu(m, var2, *grades).grid(row=i, column=2)

    # Add the gpa label, as well as the add class and calculate buttons
    button = Button(m, text="Add Class", command=lambda: add_class(m)).grid(row=6, column=0)
    button2 = Button(m, text="Calculate GPA", command=lambda: get_values(m)).grid(row=6, column=2)
    gpa_label = Label(m, text="N/A", width=25, font=("Times New Roman", 30)).grid(row=7, column=1)
    m.mainloop()


def add_class(m):
    """
    Function: add_class
    Description: This function is used in order to add another class to the UI
    :param m: The Tkinter Instance for which all the elements appear on
    :return: None
    """
    y = int(m.grid_size()[1]) - 2

    # Get rid of gpa label, add class button, and calculate button
    m.grid_slaves(y, 2)[0].destroy()
    m.grid_slaves(y, 0)[0].destroy()
    m.grid_slaves(y+1, 1)[0].destroy()

    # Add the new class fields to the bottom row
    e = Entry(m).grid(row=y, column=0)
    var = StringVar(m)
    var.set("-")
    var2 = StringVar(m)
    var2.set("-")
    o = OptionMenu(m, var, *credit_hours).grid(row=y, column=1)
    o2 = OptionMenu(m, var2, *grades).grid(row=y, column=2)

    # Add back the gpa label, add class button, and calculate button
    button = Button(m, text="Add Class", command=lambda: add_class(m)).grid(row=y+1, column=0)
    button2 = Button(m, text="Calculate GPA", command=lambda: get_values(m)).grid(row=y+1, column=2)
    gpa_label = Label(m, text="N/A", width=25, font=("Times New Roman", 30)).grid(row=y+2, column=1)


def calculate_gpa(grades_list, m):
    """
    Function: calculate_gpa
    Description: Based on the input passed by get_values, calculates the gpa and displays it on the screen
    :param grades_list: The list of tuples representing grades that were entered
    :param m: The Tkinter Instance for which all the elements appear on
    :return: None
    """
    y = int(m.grid_size()[1]) - 1

    # get rid of the current gpa label that is displayed
    m.grid_slaves(y, 1)[0].destroy()

    # the following variables are used as counters in order to calculate the final gpa
    gpa_total = 0
    hour_total = 0

    '''
    For every grade tuple that is passed in, make sure that the credit hours and the letter grade is supplied. If they
    are, then use the dictionary to convert the letter grade to a gpa, and multiply it by the number of credit hours.
    Add this to the gpa_total variable in order to store it. Increment the hour_total by the number of credit hours for
    that class. Once all grades have been considered, divide gpa_total by hour_total in order to get the overall gpa 
    '''
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

    # Display the gpa on the screen
    gpa_label = Label(m, text=gpa_total, width=25, font=("Times New Roman", 30)).grid(row=y, column=1)


def get_values(m):
    """
    Function: get_values
    Description: Parses all of the values that the user inputs, and creates a list of valid inputs to pass to
                 calculate_gpa
    :param m: The Tkinter Instance for which all the elements appear on
    :return: None
    """
    grades_list = []
    prev_child = None

    '''
    For all the drop down boxes representing both the credit hours and letter grade for the class, store their values
    as a tuple representing each class and add it to the grades_list.
    '''
    for child in m.children.values():
        info = child.grid_info()
        current_row = info['row']
        current_col = info['column']
        if 0 < int(current_row) < m.grid_size()[1]-2 and int(current_col) > 0:
            if prev_child is None:
                pass
            elif prev_child.grid_info()['row'] == current_row:
                grade = (prev_child['text'], child['text'])
                grades_list.append(grade)
            prev_child = child

    # Pass the grades_list to calculate_gpa to do the gpa calculation
    calculate_gpa(grades_list, m)


if __name__ == '__main__':
    pretty_layout()
