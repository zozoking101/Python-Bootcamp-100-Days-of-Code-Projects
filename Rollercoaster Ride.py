# Rollercoaster Ride

height = int(input("What is your height in cm? : "))
if height >= 120:
    age = int(input("How old are you? : "))
    print("You are tall enough to ride the rollercoaster!")
    if age <= 18 & age >= 12:
        print("Please pay $ 7.")
    elif age < 12:
        print("Please pay $ 5")
    elif age < 45 & age > 18:
        print("Please pay $ 12.")
    elif age >= 45:
        print("Please pay $ 3")
else:
    print("You aren/'t tall enough to ride the rollercoaster!")