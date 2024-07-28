height = input("Enter your height in meters: ")
weight = input("Enter your weight in kg: ")

height = float(height)
weight = float(weight)

bmi = weight / height**2
bmi = float(bmi)
bmi = round(bmi, 1)

if bmi >= 30:
    print(f"BMI is {bmi}")
    print("Obesity")
elif bmi >= 25 and bmi <= 29.9:
    print(f"BMI is {bmi}")
    print("Overweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print(f"BMI is {bmi}")
    print("Normal")
else:
    print(f"BMI is {bmi}")
    print("Underweight")