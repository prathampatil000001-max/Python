# def greet():
#     message = "Hello"
#     print(message)

# greet()


# def calculate_area(length, width):
#     """calculate the area of a rectangle.
    
    
#     Args:
#         length: The rectangle length.
#         width: The rectangle width 
    
    
#     Returns:
#            The area of the rectangle"""

#     """
#     this is part of function """

#     return length * width

# def greet():
#     message = "Hello"
#     print(message)

# greet()


# if True:
#     score = 50
# print(score)


# total=100
# total=90
# diff=80
# def calculate():
#     total = 10
#     print(total)
   
# calculate()
# print(total)
# print(print(total))
# print(diff)

# def show_number():
#     number = 5
#     add = number + 1
#     print(add)

# show_number()
# show_number()

# # x = 10

# # def demo():
# #     # global x
  
# #     y=20
#     x=y+1
#     print(y)
 
# demo()
# print(x)
# def show():
#     x = 10
#     print(x)
# show()

# if True:
#     score = 50
# print(score)

# def calculate():
#     total = 10
#     print(total)

# calculate()
# def show_number():
#     number = 5
#     number = number + 1
#     print(number)

# show_number()
# show_number()

# count = 100

# def show():
#     count = 5
#     print(count)

# show()
# print(count)

# x = 10

# def demo():
#     print(x)
#     x = 20

# demo()

# x = 10

# def demo():
#     print(x)
#     local_x = 20

# demo()
# x = 10

# def demo():
#     global x
#     print(x)
#     x = 20

# demo()
# print(x)

# def test():
#     value = 7
#     print(value)
# test()

# def test():
#     print(points)
#     points = 10
# test()

# item = "pen"
# def show():
#     item = "book"
#     print(item)
# show()
# print(item)
# app_name = "StudyApp"

# def show_app():
#     print(app_name)

# show_app()
# print(app_name)

# tax_rate = 0.18

# def calculate_tax(amount):
#     return amount * tax_rate

# print(calculate_tax(1000))

# score = 0

# def add_point():
#     global score
#     score = score + 1

# add_point()
# add_point()
# print(score)

# score = 0

# def add_point():
#     score = score + 1

# add_point()

# a=int(input("Enter a string:-"))
# count=0
# for i in range("string"-1):
#     count+=1
#     def calculate():
#     total = 10
#     print(total)

# calculate()

# def show_number():
#     number = 5
#     number = number + 1
#     print(number)

# show_number()
# show_number()


# i=0
# while i>=-10:
#     name="prathmesh"
#     print(i)
#     i-=1
#     print(name)

# count =100
# def show():
#     count1=count+2
# show()
# print(count)
# print(count)

# def test():
#     value = 7
#     print(value)
# test()

# app_name = "StudyApp"

# def show_app():
#     print(app_name)

# show_app()
# print(app_name)

# message="global"
# def outer():
#     def inner():
#         message=True+1
#         print(message)
#     inner()
# outer()

# score = 0

# def add_point():
#     global score
#     score = score + 1

# add_point()
# add_point()
# print(score)

# items = []

# def add_item():
#     items.append("book")

# add_item()
# print(items)

# language = "Python"
# def show():
#     print(language)
# show()

# total = 0
# def increase():
#     total += 1
# increase()

# names = []
# def add_name():
#     names.append("Asha")
# add_name()
# print(names)


def outer():
    def inner():
        print(list("prathmesh "))
    inner()
outer()

message = "global"

def outer():
    message = "enclosing"

    def inner():
        print(message)
        print(len("cat"))

    inner()

outer()


for i in range(0):
    list="PRATHAM"
    print(list("PRATHAM"))
print(list("PRATHAM"))

def make_number():
    number = 42
    return number

answer = make_number()
print(answer)

def make_list():
    values = [10, 20]
    return values

result = make_list()
result.append(30)
print(result)

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
print(counter())

for item in ["a", "b"]:
    pass

print(item)