# Get pet species
species = input("Enter the pet's species (Dog/Cat): ").capitalize()

# Get pet age
age = int(input("Enter the pet's age in years: "))

# Determine the type of pet food
if species == "Dog":
    if age < 2:
        food_recommendation = "Puppy food"
    else:
        food_recommendation = "Adult dog food"
elif species == "Cat":
    if age > 5:
        food_recommendation = "Senior cat food"
    else:
        food_recommendation = "Adult cat food"
else:
    food_recommendation = "Unknown species, please enter Dog or Cat"

print(f"Recommended pet food: {food_recommendation}")
