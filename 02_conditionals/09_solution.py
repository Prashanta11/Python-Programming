year = int(input("Enter a year: "))

# Determine if the year is a leap year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year_status = "Leap year"
else:
    leap_year_status = "Not a leap year"

print(f"The year {year} is {leap_year_status}.")
