# Q8. Movie Ticket Booking
# Create a movie booking menu:

# 1 → Morning Show
# 2 → Afternoon Show
# 3 → Evening Show
# 4 → Night Show
choice=int(input("Enter a show"))
match choice:
      case 1:
            print("Morning Show")
      case 2:
            print("Afternoon Show")
      case 3:
            print("Evening Show")
      case _:
            print("Night show")