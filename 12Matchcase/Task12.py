# Q12. User Role
# A system supports these roles:

# admin
# teacher
# student
# guest
# Display the appropriate access message.

# Example:

# admin   → Full Access
# teacher → Teacher Dashboard
# student → Student Dashboard
# guest   → Limited Access
# For an unknown role:

# Invalid Role
role =input("Enter a role :Admin, Teacher, Student,Guest,For unkonwn ")
match role:
    case "Admin":
        print("Full Access")
    case "Teacher":
        print("Teacher Dashboard")
    case"Student":
        print("Student Dashboard")
    case"Guest":
        print("Limited Access")
    case _:
        print("Invalid Role")