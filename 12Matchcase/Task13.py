# Q13. Weekday or Weekend
# Take a day number:

# 1 → Monday
# 2 → Tuesday
# 3 → Wednesday
# 4 → Thursday
# 5 → Friday
# 6 → Saturday
# 7 → Sunday
# Use match-case and | to display:

# Weekday
# for Monday to Friday and:

# Weekend
# for Saturday and Sunday.

# For any other number:

# Invalid Day
# Sample Input
day=input("Enter a Week days :-,""Monday"
 "Tuesday"
 "Wednesday"
 "Thursday"
 "Friday"
 "Saturday"
 "Sunday:-")
day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")