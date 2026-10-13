# str=input("Enter a string :")
# i=0
# j=len(str)-1
# flag=True
# while (i<j):
#     if str[i]==str[j]:
#         i+=1
#         j-=1
#     else:
#         flag=False
#         i=j
# if flag:
#     print("Given String is Palandrome..!!")
# else:
#     print("Give String is not Palandrone..!!")       


# name=(input("Enter a name"))
# for sentence in name :
#     digits==sentence.isdigit()
#     if sentence== digits:
#         print("sentence")
#     else:
#         print("digit")    

# name=input("Enter your name")
# for i in name:
#     if chr(48)<=i<=chr(57):
#         print("",end="")
#     else:
#         print(i,end="")

# a="agsfss123"
# for i in a:
#     if i.isalpha():
#         print("Is alphabets")
#     else:
#         print("have a fixed")    
# number1=input("Enter a number :")
# number2=input("Enter a number :")
# number1 = int(number1)
# number2 = int(number2)



# num1=int(input("Enter first number :"))
# num2=int(input("Enter second number :"))
# choice=int(input("Enter your choice 1.Addition 2.Subtraction 3.Multiplication 4.Division :"))
# match choice:
#     case 1:
#         print("Addition is:", num1 + num2)
#     case 2:
#         print("Subtraction is", num1 - num2)
#     case 3:
#         print("Multiplication is", num1 * num2)
#     case 4:
#             print("Division is",num1/num2)
#     case _:
#           print("Invalid choice")

# while True:
#     num1=int(input("Enter first number :"))
#     num2=int(input("Enter second number :"))
#     choice=int(input("Enter your choice 1.Addition 2.Subtraction 3.Multiplication 4.Division :"))
#     match choice:
#         case 1:
#             print("Addition is:", num1 + num2)
#         case 2:
#             print("Subtraction is", num1 - num2)
#         case 3:
#             print("Multiplication is", num1 * num2)
#         case 4:
#                 print("Division is",num1/num2)
#         case _:
#               print("Invalid choice")
#     ch=input("Do you want to continue (y/n) :")
#     if ch=='n':
#         break

# num1=int(input("Enter first number :"))
# num2=int(input("Enter second number :"))
# choice=int(input("Enter your choice 1.Addition 2.Subtraction 3.Multiplication 4.Division :"))
# match choice:
#     case 1:
#         print("Addition is:", num1 + num2)
#     case 2:
#         print("Subtraction is", num1 - num2)
#     case 3:
#         print("Multiplication is", num1 * num2)
#     case 4:
#             print("Division is",num1/num2)
#     case _:
#           print("Invalid choice")

# number=input("Enter a number :")
# choice=int(input("Enter your choice 1.Even 2.Odd 3.Prime  :"))
# match choice:
#     case 1:
#         if int(number) % 2 == 0:
#             print("The number is even.")
#         else:
#             print("The number is not even.")
#     case 2:
#         if int(number) % 2 != 0:
#             print("The number is odd.")
#         else:
#             print("The number is not odd.")
#     case 3:
#         num = int(number)
#         is_prime = True
#         if num < 2:
#             is_prime = False
#         else:
#             for i in range(2, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     is_prime = False
#                     break
#         if is_prime:
#             print("The number is prime.")
#         else:
#             print("The number is not prime.")
#     case _:
#         print("Invalid choice.")

# month = int(input("Enter a month number (1-12): "))

# match month:
#     case 1 | 2 | 3 | 4 | 5| 6 | 7 | 8 | 9 | 10:
#         print("good month")
#     case 11| 12:
#         print("worse month")
#     case _:
#         print("Invalid")



# marks = 20

# match marks:
#     case a if a>= 90:
#         print("A")
#     case b if b >= 75:
#         print("B")
#     case x if x >= 60:
#         print("C")
#     case x if x >= 40:
#         print("D")
#     case x if x < 40:
#         print("E")
#     case _:
#         print("Fail")


# ///////---------------Nested match case question----/////
# /////-----Gas Booking case-----///////// 

# gas_type = input("Enter gas type (domestic/commercial): ")

# match gas_type:
#     case "domestic":
#         booking = input("Enter booking type (new/refill): ")

#         match booking:
#             case "new":
#                 print("New domestic gas connection selected.")
#             case "refill":
#                 print("Domestic gas refill booking confirmed.")
#             case _:
#                 print("Invalid domestic booking type.")

#     case "commercial":
#         booking_type = input("Enter booking type (new/refill): ")

#         match booking_type:
#             case "new":
#                 print("New commercial gas connection selected.")
#             case "refill":
#                 print("Commercial gas refill booking confirmed.")
#             case _:
#                 print("Invalid commercial booking type.")

#     case _:
#         print("Invalid gas type.")

#////////-------------Guard Practice-------//////
# These questions introduce case ... if ... (guards). Read them carefully.

# day = 4

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("friday")
#     case 5:
#         print("satrday")
#     case _:
#         print("Invalid Day")       
# day = 10

# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6 | 7 | 8 | 9 |10:
#         print("Weekend")
#     case _:
#         print("Invalid Day")

# marks = 82

# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 60:
#     print("C")
# elif marks >= 40:
#     print("D")
# else:
#     print("Fail")


# choice = int(input("Enter your choice: "))

# match choice:
#     case 1:
#         print("Addition")
#     case 2:
#         print("Subtraction")
#     case 3:
#         print("Multiplication")
#     case 4:
#         print("Division")
#     case _:
#         print("Invalid Choice")


# account = "student"
# choice = 2

# match account:

#     case "student":

#         match choice:
#             case 1:
#                 print("View Courses")
#             case 2:
#                 print("View Marks")
#             case 3:
#                 print("View Attendance")
#             case _:
#                 print("Invalid Choice")

#     case "teacher":

#         match choice:
#             case 1:
#                 print("View Students")
#             case 2:
#                 print("Enter Marks")
#             case _:
#                 print("Invalid Choice")

#     case _:
#         print("Invalid Account Type")
# if marks >= 90:
#     print("A")
# elif marks >= 75:
#     print("B")
# elif marks >= 60:
#     print("C")
# else:
#     print("Fail")

# str=input("Enter a string")
# flag=True
# count=0
# for ch in str:
#     count+=1
#     if ch=="o":
#         flag=False
#         print("Found")
#     else:
#         print("Not  Found")

s = input("Enter a string: ")
flag = True
count = 0

for i in range(len(s)):
    count += 1

for i in range(len(s)):
    if s[i] == "o":
        flag = False
        print("Found")
        break

if flag:
    print("Not Found")

print("Count =", count)

# Topic 11 — Mixed Logic Challenge
# Q39. Employee Portal
# Create an employee portal.

# Main menu:

# 1 → Employee
# 2 → Manager
# Employee options:

# 1 → View Profile
# 2 → Apply Leave
# 3 → View Salary
# Manager options:

# 1 → View Team
# 2 → Approve Leave
# 3 → View Reports
# Use nested match-case.

# For the Apply Leave option, ask for the number of leave days.

# Use if to check:

# If leave days are greater than 0, display Leave Request Submitted.
# Otherwise display Invalid Leave Days.
# This problem should use both match-case and if.

for i in range(1,8):
    if i ==2:
        break
    print(i)

# Print numbers from 1 to 10, but stop when the number becomes 6
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# numbers = [10, 20, 30, 40, 50]
# Search for 30.
numbers = [10, 20, 30, 40, 50]

target = 30

if target in numbers:
    print("Found at index:", numbers.index(target))
else:
    print("Not found")

# Problem 3
# Take numbers from the user continuously.

# Stop when the user enters 0.
while True:
    num = int(input("Enter a number: "))

    if num == 0:
        print("Program stopped.")
        break

#   Problem 4
# Print numbers from 1 to 100, but stop when you reach the first number divisible by 17.

  
for i in range(1, 101):
    print(i)
    if i % 17 == 0:
        break