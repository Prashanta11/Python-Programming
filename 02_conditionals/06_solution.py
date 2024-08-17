distance = float(input("Enter the distance in kilometers: "))

if distance < 3:
    transportation = "Walk"
elif distance <= 15:
    transportation = "Bike"
else:
    transportation = "Car"

print(f"Suggested mode of transportation: {transportation}")
