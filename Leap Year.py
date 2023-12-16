# Leap Year

year = int(input("Which year do you want to check? : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap.")
        else:
            print("Not divisible by 400. Not Leap.")
    elif year % 400 != 0 and year % 100 != 0:
        print("Leap.")
else:
    print("Not divisible by 4. Not Leap.")
