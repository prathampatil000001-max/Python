#IPO
# input
# input three number
# processing 
# then number check largest number
# output


# Algorithom

# start
# read first number
# read second number
# read third number
# check largest number
# print result
# stop

# python

a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b and a>c:
    print(f"{a} is a largest number")
elif b>a and b>c:
    print(f"{b} is a largest number")
else:
    print(f"{c} is a largest number")