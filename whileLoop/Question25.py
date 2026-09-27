# 25.
# Take a string from the user and count how many characters are uppercase letters.
variable=(input("Enter a string"))
count=0
num=0
while count<len(variable):
    print(variable[count],end="")
    if 'A'<=variable[count]<='Z':
       num+=1
    count+=1
    
print(num)