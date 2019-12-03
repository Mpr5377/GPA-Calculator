"""
File Name: Calculator_Logic.py
Name: Matt Robinson
Description: This is just going to be a small program to test the logic for calculating GPA
"""


grades = {
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


def calculate_gpa(file):
    """
    Function: calculate_gpa()
    Parameters: file - Text file to take in letter grade values to be converted
    :return GPA Value on a 4.0 Scale
    Description: Does the following Math to return the GPA value on a 4.0 Scale:

    GPA MATH:
        SUMMATION of (Grade * Credit Hours)
        ----------------------------------- = GPA
                   Credit Hours
    """
    # total_credit_hours will be used as a counter variable to keep track of the total number of credit hours taken
    total_credit_hours = 0

    # total_weight will be used to keep track of the summation of the Grade * Credit Hours for each class
    total_weight = 0

    # Open the file that is passed in as read only
    f = open(file, "r")

    # Read the first line to avoid headers in the for loop
    f.readline()

    # Parse each line in the file collecting the Letter Grade and the Credit Hours
    for line in f:
        # Split the line on the ","
        line_array = line.strip().split(",")

        # Set weight = to the letter grade gpa value multiplied by the credit hours
        weight = grades.get(line_array[1]) * line_array[2]

        # Increment the total weight by this classes weight
        total_weight += weight

        # Increment the total credit hours by the number of credit hours of this class
        total_credit_hours += line_array[2]

    gpa = total_weight / total_credit_hours

    return gpa


if __name__ == '__main__':
    total_gpa = calculate_gpa("Test_Files/Test1.csv")
    print(total_gpa)
