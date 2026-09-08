#Question no.02

numb=int(input("Enter Any Number"))
if numb>0 and numb%2==0:
    print(" Possitive Even")
elif numb>0 and numb%2!=0:
    print("Possitive Odd")
elif numb<0 and numb%2==0:
    print("Negative Even")
elif numb<0 and numb%2!=0:
    print("Negative Even")
else :
    print("Zero")