num=int(input("Enter Your Number:"))
if num%3==0 and num%7==0:
    print("Divisible by both 3 and 7")
elif num%3==0 :
    print("Divisible by 3")
elif num%7==0:
    print("Divisible by 7")
else :
    print("Divisible by neither")