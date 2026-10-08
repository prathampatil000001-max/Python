# Topic 3 — String-Based Real-Life Problems
# Q9. Weather Advice
# Take the weather condition as input:

# sunny
# rainy
# cloudyDisplay appropriate advice:
# snowy
# sunny  → Wear sunglasses
# rainy  → Carry an umbrella
# cloudy → Weather may change
# snowy  → Wear warm clothe


choice=(input("Enter a season : ,sunny, rainy,cloudy, snowy"))
match choice:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Carry an umbrella")
    case "cloudy":
        print("Weather may change")
    case "snowy":
        print("Wear warm clothe")
