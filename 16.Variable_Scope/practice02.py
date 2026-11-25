count=0
def counter_fun(n):
    global count
    count+=1

    if (count==5):
        return count 

    return counter_fun(n+1)

print(counter_fun(1))