# Q2. Mobile Settings
# Create a simple mobile settings menu:

# 1 → Wi-Fi
# 2 → Bluetooth
# 3 → Mobile Data
# 4 → Airplane Mode
# 5 → Exit
# Take the user's choice and display the selected setting.

# For an invalid choice, display:

# Invalid Setting

choice=2

match choice:
        case 1:
            print("wi-Fi")
        case 2:
            print("Blutooth")
        case 3:
          print("Mobile Data")
        case 4:
          print("Airplane made")    
        case 5:
          print("Exit")
        case 6:
            print("Invalid setting")