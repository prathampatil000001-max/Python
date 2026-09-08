num1=int(input("Enter the 1st number :"))
num2=int(input("Enter the 2nd number :"))
num3=int(input("Enter the 3rd number :"))
if num1<num2 and num1<num3:
    print(f"The smaller number is {num1}")
elif num2<num1 and num2<num3:
    print(f"The smaller number is {num2}")
elif num3<num1 and num3<num2:
    print(f"The smaller number is {num3}")
else :
    print("Does not possible")  