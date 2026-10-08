# Q10. Payment Method
# An online store accepts:

# upi
# card
# cash
# wallet
# Display the selected payment method.

choice=int(input("Enter a mathod of payment no:"))
match choice :
    case 1:
        print("UPI Payment method selected")
    case 2:
        print("Cash Payment method selected")
    case _:
        print("wallet Payment method selected")
        