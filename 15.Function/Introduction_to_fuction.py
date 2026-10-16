# 13. Coding Practice Problems
# Solve these using only the concepts taught in this lesson. Do not use parameters, arguments, or return yet.

# Basic Level
# 01] Define a function named greet that prints Hello, Python!. Call it once.

def greet():
    print("Hello, Python!")

greet()

# 02] Define a function named show_name that prints your name. Call it three times.
def show_name():
    print("Prathmesh..!!")

show_name()
show_name()
show_name()

#  03] Define a function named show_name that prints your name. Call it three times.
def print_line():
    print("-" * 20)

print_line()
print("Welcome to CodingGita ")
print_line()

# 04] Define a function named show_rules that prints three classroom rules, one per line.
def show_rules():
    print("Be respectful to everyone.")
    print("Raise your hand before speaking.")
    print("Keep the classroom clean.")

show_rules()

# 05] Define a function named show_square that prints a 4-by-4 square of * characters using four print("****") statements. Call it once.
def show_square():
    print("****")
    print("****")
    print("****")
    print("****")

show_square()

# 06] Define a function named show_menu that prints three menu options. Call it twice.
def show_menu():
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

show_menu()
show_menu()

# 07] Define two functions, morning_message and evening_message. Call them in the reverse order of their definitions
def morning_message():
    print("Good morning!")

def evening_message():
    print("Good evening!")

evening_message()
morning_message()

# 08] Define a function named show_student_card that prints a heading, a student name, and a roll number. Call it once.
def show_student_card():
    print("Student Card")
    print("Name: Rahul")
    print("Roll Number: 101")

show_student_card()

# Define a function named print_numbers that prints the numbers 1 through 5 using five print statements. Call it twice.

def print_numbers():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)

print_numbers()
print_numbers()

# Define a function named show_pattern that prints:
# *
# **
# ***
# Call it twice.

def show_pattern():
    print("*")
    print("**")
    print("***")

show_pattern()
show_pattern()

# Intermediate Level
# 11] Create three functions: show_header, show_body, and show_footer. Call them in the correct order to print a simple report.

def show_header():
    print("===== Report =====")

def show_body():
    print("This is the report body.")

def show_footer():
    print("===== End of Report =====")

show_header()
show_body()
show_footer()

# 12] Create a function named show_separator that prints ====================. Use it between sections of a report.

def show_separator():
    print("====================")

print("Report Header")
show_separator()
print("Report Body")
show_separator()
print("Report  Footer")

# 13]Define functions named step_one, step_two, and step_three. Each should print its step name. Call them in the order 3, 1, 2.
def step_one():
    print("Step One")

def step_two():
    print("Step Two")

def step_three():
    print("Step Three")

step_three()
step_one()
step_two()

# 14]Create a function named show_separator that prints ====================. Use it between sections of a report.
def show_separator():
    print("====================")

print("Report Header")
show_separator()
print("Report Body")
show_separator()
print("Report Footer")

# 15] Define a function that prints five stars on one line. Call it four times to create four rows
def print_stars():
    print("*****")

print_stars()
print_stars()
print_stars()
print_stars()

# 16] Create a function named show_welcome that prints a welcome message and course name. Call it at the start of a simple program.
def show_welcome():
    print("Welcome!")
    print("Course: Python Programming")

show_welcome()

print("Let's start learning Python.")

# 17]Define a function named show_help that prints instructions for a simple calculator. Call it before printing the calculator menu. 
def show_help():
    print("Welcome to the Simple Calculator!")
    print("Instructions:")
    print("1. Choose an operation from the menu.")
    print("2. Enter the numbers when prompted.")
    print("3. The calculator will display the result.")
    print("4. Choose Exit to quit the calculator.")

show_help()

print("--- Calculator Menu ---")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exit")

# 18] Create two functions that print the opening and closing lines of a receipt. Call them around the receipt details.
def print_receipt_header():
    print("================================")
    print("          STORE RECEIPT")
    print("================================")

def print_receipt_footer():
    print("================================")
    print("       Thank you for shopping!")
    print("================================")
print_receipt_header()

print("Item:       Notebook")
print("Quantity:   2")
print("Price:      ₹50")
print("Total:      ₹100")

print_receipt_footer()

# 19]Define a function named print_box that prints a fixed three-line text box. Call it twice.
def print_box():
    print("+----------+")
    print("|  Hello!  |")
    print("+----------+")

print_box()
print_box()

# 20] Create functions for a program's title, menu, and closing message. Arrange the calls to produce a readable program flow.
def print_title():
    print("==============================")
    print("      WELCOME TO MY PROGRAM")
    print("==============================")

def print_menu():
    print("--- MAIN MENU ---")
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

def print_closing():
    print("==============================")
    print("   Thank you for using the program!")
    print("==============================")
print_title()
print_menu()
print_closing()
