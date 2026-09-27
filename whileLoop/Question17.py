# Take n from the user and calculate the sum of all even numbers from 1 to n.
num=int(input("Enter a number "))
count=0
sum=0
while count<=num-1:
    
    count+=2

    sum+=count
    print(count)
print(sum )
