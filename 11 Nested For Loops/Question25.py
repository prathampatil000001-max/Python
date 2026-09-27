# 25. Repeated Row Number Pattern
# Write a Python program to print:

# 11111
# 22222
# 33333
# 44444
# 55555
# Hint
# Outer loop decides which number is printed.
# Inner loop prints the same number 5 times.
# Move to the next number after completing each row.
# Loop from 1 to 5
for i in range(1, 6):
    
   
    print(str(i) * 5)
