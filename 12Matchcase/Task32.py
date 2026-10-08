# Q32. School Management System
# Create a school management system.

# First select:

# 1 → Student
# 2 → Teacher
# 3 → Parent
# Student options:

# 1 → Marks
# 2 → Attendance
# 3 → Homework
# Teacher options:

# 1 → Enter Marks
# 2 → Attendance
# 3 → Assign Homework
# Parent options:

# 1 → Child Marks
# 2 → Child Attendance
# 3 → Contact Teacher
# Use nested match-case.

user_type = int(input("Enter your choice: "))

match user_type:

    case 1:
        print("1. Marks")
        print("2. Attendance")
        print("3. Homework")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Marks Selected")
            case 2:
                print("Attendance Selected")
            case 3:
                print("Homework Selected")
            case _:
                print("Invalid Option")

    case 2:
        print("1. Enter Marks")
        print("2. Attendance")
        print("3. Assign Homework")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Enter Marks Selected")
            case 2:
                print("Attendance Selected")
            case 3:
                print("Assign Homework Selected")
            case _:
                print("Invalid Option")

    case 3:
        print("1. Child Marks")
        print("2. Child Attendance")
        print("3. Contact Teacher")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Child Marks Selected")
            case 2:
                print("Child Attendance Selected")
            case 3:
                print("Contact Teacher Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Choice")