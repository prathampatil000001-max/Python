# Q14. Customer Support Priority
# A support system receives priority numbers:

# 1 → Low
# 2 → Medium
# 3 → High
# 4 → Critical
# Treat priorities 1 and 2 as:

# Normal Priority
# Treat priorities 3 and 4 as:

# Urgent Priority
# Use | where appropriate.
service=int(input("Enter a priority""low""Medium""High""Critical:-  "))

match service:
    case 1|2:
        print("normal ")
    case 3|4:
        print("Urgent")
    case 5:
        print("invalid")

