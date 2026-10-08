# Q3. ATM Main Menu
# Create an ATM menu:

# 1 → Check Balance
# 2 → Withdraw Money
# 3 → Deposit Money
# 4 → Change PIN
# 5 → Exit
choice=4
match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw Money") 
    case 3:
        print("Deposite Money") 
    case 4:
        print("Change PIN ")
    case _:
        print("Exit")
    