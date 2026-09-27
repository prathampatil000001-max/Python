# Take a number n and calculate:

# 1 × 2 × 3 × ... × n
num=int(input("Enter a number"))
count=1
while count<=10:
    print(count*num,end="")
    count+=1