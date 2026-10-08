# Q7. Banking Service Selection
# A banking application provides:

# 1 → Account Balance
# 2 → Mini Statement
# 3 → Fund Transfer
# 4 → Bill Payment
# 5 → Customer Support
# Write a program using match-case to display the selected service.
choice=int(input("Enter a statement"))
match choice:
    case 1:
        print("Account Balance")
    case 2:
        print("Mini Statement")
    case 3:
        print("Fund Transfer")
    case 4:
        print("Bill Payment")
    case _:
        print("Customer Support")