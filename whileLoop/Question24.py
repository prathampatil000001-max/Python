# 24.
# Take a string from the user and count how many times the character "a" appears.
variable=(input("Enter a string"))
count=0
num=0
while count<len(variable):
    print(variable[count],end="")
    if variable[count]=='a':
       num+=1
    count+=1
    
print(num)