# Tip Calculator

print("Welcome to the tip calculator")  
total_bill = float(input("What was the total bill?: $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? : "))
number = int(input("How many people to split the bill? : "))

bill = round(((percentage / 100 + 1) * total_bill)/number,2)

print(f"\nEach person should pay: ${bill:.2f}")