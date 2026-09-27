# Create a multiplication-table grid using nested for loops.
count=1
variable=1
for i in range(1, 11):
    
    for j in range(1, 11):
        
        product = i * j
        
        print(f"{product:4}",end="" )
        variable+=1
    count+=1
    print()

    
