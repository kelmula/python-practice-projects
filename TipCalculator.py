bill_amount = float(input("Enter bill amount in dollars and cents notation (must be greater than 0): "))
while bill_amount <= 0:
    bill_amount = float(input("Enter bill amount in dollars and cents notation (must be greater than 0): "))

tip_percentage = int(input("Enter the percentage of the bill you want to leave as a tip (0-100): "))
while not (0 <= tip_percentage <= 100):
    tip_percentage = int(input("Enter the percentage of the bill you want to leave as a tip (0-100): "))

tip_amount = float(bill_amount * (tip_percentage / 100.0))
total_amount = round(bill_amount + tip_amount, 2)
print(f"You have chosen to tip ${round(tip_amount, 2):.2f}.")
print(f"Your total after the tip will be ${total_amount:.2f}.")