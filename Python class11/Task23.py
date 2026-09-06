age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (True/False): ") == "True"

if age >= 18 and has_id:
    print("Allowed")
