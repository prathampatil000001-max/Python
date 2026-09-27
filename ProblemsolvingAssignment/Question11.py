# 11. Username Analyzer
# Take 5 usernames.

# For every username:

# Check length.
# Check first character.
# Count digits.
# Count underscores.
# Detect invalid special characters.
# Classify each username as:

# "Valid"
# "Needs Improvement"
# "Invalid"



for i in range(5):
    username = input(f"Enter username {i + 1}: ")

    length = len(username)
    digit_count = 0
    underscore_count = 0
    invalid_special = False

    
    if length > 0 and (username[0].isalpha() or username[0] == "_"):
        first_char_valid = True
    else:
        first_char_valid = False

    
    for ch in username:
        if ch.isdigit():
            digit_count += 1
        elif ch == "_":
            underscore_count += 1
        elif not ch.isalpha():
            invalid_special = True

    
    if length < 5 or invalid_special or not first_char_valid:
        result = "Invalid"
    elif length >= 8 and digit_count >= 1:
        result = "Valid"
    else:
        result = "Needs Improvement"

    print("\nUsername:", username)
    print("Length:", length)
    print("First character:", username[0] if length > 0 else "None")
    print("Digits:", digit_count)
    print("Underscores:", underscore_count)
    print("Invalid special character:", invalid_special)
    print("Classification:", result)
    print()
