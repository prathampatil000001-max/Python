num=int(input("Enter your number:"))
if num%5==0 and num%11==0:
    print("Divisible by both 5 and 11")
elif num%5==0:
    print("Divisible by 5 only")
elif num%11==0:
    print("Divisible by 11 only")
else:
    print("Divisible by None")