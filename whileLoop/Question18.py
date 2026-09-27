# 18.
# Take n from the user and calculate the sum of all odd numbers from 1 to n.
num=int(input("Enter a number"))
count=1
sum=1
while count<=num-2:
    count+=2
    sum+=count
    print(count)
print(sum)