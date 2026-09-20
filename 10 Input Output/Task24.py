#Question no .24


username = input("Enter username: ")
password = input("Enter password: ")

if username != "admin":
    print("User not found")
elif password != "python123":
    print("Wrong password")
else:
    print("Login successful")
