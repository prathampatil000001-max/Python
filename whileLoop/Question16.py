# D. Calculation Problems
# 16.
# Take n from the user and calculate:

# 1 + 2 + 3 + ... + n
num=int(input("Enter a number"))
count=0
sum=0
while count<=num-1:
    count+=1
    print(count)
    sum+=count
print(sum)   
