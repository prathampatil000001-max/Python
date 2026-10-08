# Q4. Traffic Signal
# Take a traffic signal color as input:

# red
# yellow
# green
# Use match-case to display:

# red    → Stop
# yellow → Wait
# green  → Go
# For any other color:


choice = (input("Enter choice colour:red, yellow, Green,other "))

match choice:
    case "red":
        print("stop")
    case "yellow":
        print("Wait")
    case "Green":
        print("Go")
    case _:
        print("For any other colour")

