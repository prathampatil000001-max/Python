# Topic 5 — Nested match-case

# Q16. University Portal
# Create a university portal.

# First ask the user to select:

# 1 → Student
# 2 → Teacher
# If the user selects Student, show:

# 1 → View Courses
# 2 → View Marks
# 3 → View Attendance
# If the user selects Teacher, show:

# 1 → View Students
# 2 → Enter Marks
# 3 → View Attendance
# Use nested match-case.

# Sample Input
# Enter user type: 1
# Enter option: 2
# Sample Output
# Opening Student Marks
user_type = int(input("Enter user type: "))

match user_type:
    case 1:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case _:
                print("Invalid option")

    case 2:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Teacher Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case _:
                print("Invalid option")

    case _:
        print("Invalid user type")

