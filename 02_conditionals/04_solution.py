color = input("Enter the color of the banana: ").lower()

if color == "green":
    ripeness = "Unripe"
elif color == "yellow":
    ripeness = "Ripe"
elif color == "brown":
    ripeness = "Overripe"
else:
    ripeness = "Unknown ripeness"

print(f"The banana is {ripeness}.")
