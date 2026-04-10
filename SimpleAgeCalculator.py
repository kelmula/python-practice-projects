current_year = 2026
birth_year = int(input("Enter the year you were born: "))
age = current_year - birth_year
if 0 <= age <= 1:
    print(f"You are approximately 1 year old.")
elif age > 1:
    print(f"You are approximately {age} years old.")
else:
    print("You did not enter a valid birth year.")
