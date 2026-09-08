name1 = input("Enter first person's name: ")
age1 = int(input("Enter first person's age: "))

name2 = input("Enter second person's name: ")
age2 = int(input("Enter second person's age: "))

name3 = input("Enter third person's name: ")
age3 = int(input("Enter third person's age: "))

if age1 <= age2 and age1 <= age3:
    youngest = name1
    youngest_age = age1
elif age2 <= age1 and age2 <= age3:
    youngest = name2
    youngest_age = age2
else:
    youngest = name3
    youngest_age = age3

print("Youngest person:", youngest)
print("Age:", youngest_age)
