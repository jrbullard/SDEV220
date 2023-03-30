# Jordan Bullard
# GPA Sorter
# This app will take a student's name and GPA and output if they made the honor roll or dean's list.
lName = input("Enter the student's last name or ZZZ to quit: ")
while lName != "ZZZ":
    fName = input("Enter the student's first name: ")
    GPA = float(input("Enter the student's GPA: "))
    if GPA >= 3.5:
        print("The student has made the Dean's List.")
    if GPA >= 3.25:
        print("The student has made the Honor Roll.")
    lName = input("Enter another student's last name or ZZZ to quit: ")