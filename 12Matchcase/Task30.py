# Q30. Food Delivery Order Status
# Take an order status:

# placed
# confirmed
# preparing
# out_for_delivery
# delivered
# cancelled
# Display a suitable message for each status.

# Example:

# Enter status: out_for_delivery
# Output:

# Your order is on the way
status = input("Enter status: ")

match status:
    case "placed":
        print("Your order has been placed.")
    case "confirmed":
        print("Your order has been confirmed.")
    case "preparing":
        print("Your order is being prepared.")
    case "out_for_delivery":
        print("Your order is on the way.")
    case "delivered":
        print("Your order has been delivered.")
    case "cancelled":
        print("Your order has been cancelled.")
    case _:
        print("Invalid order status.")

