# 2. Student Performance Analyzer
# Take marks of 10 students using a for loop.

# For each student:

# Print "Fail" if marks are below 35.
# Print "Pass" for 35–49.
# Print "Good" for 50–74.
# Print "Excellent" for 75–100.
# At the end, print the number of students in each category.


count_fail=0
count_pass=0
count_good=0
count_Excellent=0


for i in range(0,10):
    marks=int(input("Enter your marks:"))
    if marks<35:
        print("Fail")  
        count_fail+=1
    elif 35<marks<50:
        print("pass")
        count_pass+=1
    elif 50<marks<75:
        print("Good")
        count_good+=1
    elif 75<marks<=100:
        print("Excellent")
        count_Excellent+=1
    else:
        print("Go to back and inter your valid marks")

print(f"The number of Fail students are {count_fail}")
print(f"The number of Pass students are {count_pass}")
print(f"The number of Good students are {count_good}")
print(f"The number of  Excellent students are {count_Excellent} ")


