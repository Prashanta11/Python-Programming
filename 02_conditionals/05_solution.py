weather = input("Enter the current weather (Sunny, Rainy, Snowy): ").lower()

if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Read a book"
elif weather == "snowy":
    activity = "Build a snowman"
else:
    activity = "Stay indoors and relax"

print(f"Suggested activity: {activity}")
