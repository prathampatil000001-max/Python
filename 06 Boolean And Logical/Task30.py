
values = [0, 1, "", "Python", False, None]

for value in values:
    print(value, "→ Type:", type(value).__name__, "| Truthy:", bool(value))
