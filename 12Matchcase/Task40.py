# main_choice = input("Enter your choice: ")

match Main_choice:
    case "1":
        print("\n--- Student Menu ---")
        print("1. Profile")
        print("2. Marks")
        print("3. Attendance")
        print("4. Courses")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("Student Profile")
            case "2":
                print("Student Marks")
            case "3":
                print("Student Attendance")
            case "4":
                print("Student Courses")
            case _:
                print("Invalid Student choice.")

    case "2":
        print("\n--- Teacher Menu ---")
        print("1. Students")
        print("2. Enter Marks")
        print("3. Attendance")
        print("4. Courses")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("Student List")
            case "2":
                print("Enter Student Marks")
            case "3":
                print("Student Attendance")
            case "4":
                print("Teacher Courses")
            case _:
                print("Invalid Teacher choice.")

    case "3":
        print("\n--- Administration Menu ---")
        print("1. Fees")
        print("2. Admissions")
        print("3. Notices")
        print("4. Departments")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("Fees Section")
            case "2":
                print("Admissions Section")
            case "3":
                print("Notices Section")
            case "4":
                print("Departments Section")
            case _:
                print("Invalid Administration choice.")

    case _:
        print("Invalid main menu choice.")