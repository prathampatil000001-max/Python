# Topic 2 — Practical Menu Systems

# Q5. Student Portal
# Create a student portal menu:

# 1 → View Profile
# 2 → View Courses
# 3 → View Marks
# 4 → View Attendance
# 5 → Logout
# Take the user's choice and display an appropriate message.

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You selected View Profile.")
    case 2:
        print("You selected View Courses.")
    case 3:
        print("You selected View Marks.")
    case 4:
        print("You selected View Attendance.")
    case 5:
        print("Logged out successfully.")
    case _:
        print("Invalid choice. Please select 1-5.")

