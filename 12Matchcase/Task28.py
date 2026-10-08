# 28. Railway Ticket System
# Create a railway ticket menu:

# 1 → Book Ticket
# 2 → Cancel Ticket
# 3 → Check PNR
# 4 → Train Schedule
# 5 → Exit
# Display the appropriate action.
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Book Ticket selected.")
elif choice == 2:
    print("Cancel Ticket selected.")
elif choice == 3:
    print("Check PNR selected.")
elif choice == 4:
    print("Train Schedule selected.")
elif choice == 5:
    print("Exiting Railway Ticket System...")
else:
    print("Invalid choice.")