# Marks=int(input("Enter your marks:"))

# if Marks>=90:
#     print("Grade A")
# if Marks>60 and Marks<=90:
#     print("Grade B")


# if Marks<60:
#     print("Fail")        
operation=input("Choose the given serial number for the operation you want to perform:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")

if operation=="1" or operation=="2" or operation=="3" or operation=="4":

    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))

    if operation=="1":
        print("Addition of two numbers is:",num1+num2)
    elif operation=="2":
        print("Subtraction of two numbers is:",num1-num2)
    elif operation=="3":
        print("Multiplication of two numbers is:",num1*num2)
    elif operation=="4":
        print("Division of two numbers is:",num1/num2)
else:
    print("sorry..!! you have entered wrong serial number for the operation you want to perform")    

