# count=0
# def counter_fun(n):
#     global count
#     count+=1

#     if (count==5):
#         return count 

#     return counter_fun(n+1)

# print(counter_fun(5))

add =0
def addition_of_num(n):
    global add 
    add+=n
    if(n==10):
        return add 
    return addition_of_num(n+1)
print(addition_of_num(1))


# def countdown(n):
#     if n == 0:
#         print("Done")
#         return

#     print(n)
#     return countdown(n + 1)

# countdown(3)