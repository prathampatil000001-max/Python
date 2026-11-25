count=0
def counter_fun(n):
    global count
    count+=1

    if (count==5):
        return count 

    return counter_fun(n+1)

print(counter_fun(1))

def countdown(n):
    if n == 0:                 # Base case
        print("Done!")
        return

    print(n)
    countdown(n - 1)           # Recursive case

countdown(3)

def countdown(n):
    if n == 0:
        print("Done")
        return

    print(n)
    countdown(n - 1)

countdown(0)