# 4. Password Batch Validator
# Take passwords for 5 users using a for loop.

# For every password, check:

# Minimum length of 8.
# At least one uppercase letter.
# At least one lowercase letter.
# At least one digit.
# At least one special character.
# Print "Strong", "Medium", or "Weak" based on the number of conditions satisfied.



for i in range(5):
    password = input(f"Enter password for user {i + 1}: ")

    conditions = 0

    
    if len(password) >= 8:
        conditions += 1

    
    if any(ch.isupper() for ch in password):
        conditions += 1

    
    if any(ch.islower() for ch in password):
        conditions += 1


    if any(ch.isdigit() for ch in password):
        conditions += 1

    
    if any(not ch.isalnum() for ch in password):
        conditions += 1

    if conditions == 5:
        result = "Strong"
    elif conditions >= 3:
        result = "Medium"
    else:
        result = "Weak"

    print("Password strength:", result)
