# BMI Calculator

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal Weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

bmi = calculate_bmi(weight, height)
print("Your BMI:", round(bmi, 2))
print("Category:", classify_bmi(bmi))
