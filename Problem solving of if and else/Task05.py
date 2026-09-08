#Question no.05
num1=int(input("Enter the 1sr number:") )
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))
if num1>num2 and num1>num3:
    print(f"The largest number is {num1}")
elif num2>num1 and num2>num3:
    print(f"The largest nuber is {num2}")
elif num3>num1 and num3>num2:
    print(f"The largest number is {num3}")
else:
    print("invalid input")