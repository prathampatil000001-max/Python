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


gas_type = input("Enter gas type (domestic/commercial): ")

match gas_type:
    case "domestic":
        booking = input("Enter booking type (new/refill): ")

        match booking:
            case "new":
                print("New domestic gas connection selected.")
            case "refill":
                print("Domestic gas refill booking confirmed.")
            case _:
                print("Invalid domestic booking type.")

    case "commercial":
        booking_type = input("Enter booking type (new/refill): ")

        match booking_type:
            case "new":
                print("New commercial gas connection selected.")
            case "refill":
                print("Commercial gas refill booking confirmed.")
            case _:
                print("Invalid commercial booking type.")

    case _:
        print("Invalid gas type.")
