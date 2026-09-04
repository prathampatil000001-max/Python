

age = input("Enter your age: ")
print(age)

name = "Rahul"

print(name)

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)
