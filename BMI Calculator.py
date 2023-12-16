# BMI Calculator

w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in m: "))
bmi = round(w/(h**2),1)

if bmi < 18.5:
    print(f"Your BMI is: {bmi:.1f} . You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is: {bmi:.1f} . You have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is: {bmi:.1f} . You are overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is: {bmi:.1f} . You are obese.")
else:
    print(f"Your BMI is: {bmi:.1f} . You are clinically obese.")
