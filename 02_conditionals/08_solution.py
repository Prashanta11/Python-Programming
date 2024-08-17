password = input("Enter your password: ")

# Determine the strength of the password
if len(password) < 6:
    strength = "Weak"
elif 6 <= len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Your password is: {strength}")
