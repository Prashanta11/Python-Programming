age = int(input("Enter your age: "))
day = "wednesday"

# Determine base ticket price
if age >= 18:
    price = 12
else:
    price = 8

if day == "wednesday":
    price -= 2

print("Ticket price for you is:$",price)