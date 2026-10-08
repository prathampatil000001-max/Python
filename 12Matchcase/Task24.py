# Q24. Online Exam Portal
# Create a menu:

# 1 → Start Exam
# 2 → View Result
# 3 → Exit
# If the user selects Start Exam, ask for age.

# Use if to check whether the student is at least 18 years old.

# Sample Input
# Enter choice: 1
# Enter age: 20
# Sample Output
# You can start the exam
choice = int(input("Enter choice: "))

match choice:
    case 1:
        age = int(input("Enter age: "))

        if age >= 18:
            print("You can start the exam")
        else:
            print("You cannot start the exam")

    case 2:
        print("View Result")

    case 3:
        print("Exit")

    case _:
        print("Invalid choice")
