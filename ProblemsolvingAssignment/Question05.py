# 5. Sentence Word Analyzer
# Take a sentence and examine every word.

# For each word:

# Print its length.
# Print "Short" if length ≤ 3.
# Print "Medium" if length is 4–6.
# Print "Long" if length > 6.
# At the end, print the number of short, medium, and long words.

para=input("Write a paragraph")
for i in range(0,1):
    if len(para)<=3:
        print("Short" ,end="")
    elif 4<= (len(para)) <=6:
        print("Medium",end="")
    else:
        print("Long",end="")
print()