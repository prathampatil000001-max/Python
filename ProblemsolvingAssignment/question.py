choice = 3

match choice:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other")


def show():
    x = 10
    print(x)
show()

def show():
    x = 10
    print(x)
show()

def show_number():
    number = 5
    number = number + 1
    print(number)

show_number()
show_number()

count = 100

def show():
    count = 5
    print(count)

show()
print(count)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)