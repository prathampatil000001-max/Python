# Topic 8 — Real-World Application Problems
# Q26. Smart Home Controller
# Create a smart home controller:

# 1 → Light
# 2 → Fan
# 3 → AC
# 4 → TV
# For each device, display an appropriate message.

# Example:

# Enter device: 3

# AC Controller Opened
device = int(input("Enter device: "))

match device:
    case 1:
        print("Light Controller Opened")

    case 2:
        print("Fan Controller Opened")

    case 3:
        print("AC Controller Opened")

    case 4:
        print("TV Controller Opened")

    case _:
        print("Invalid Device")
