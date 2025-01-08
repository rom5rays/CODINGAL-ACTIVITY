def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: BMI = weight (kg) / height (m)^2
    """
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)  # Round to 2 decimal places
    except ZeroDivisionError:
        return "Height cannot be zero!"

# Input weight and height
try:
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Output BMI and category
    if isinstance(bmi, float):
        print(f"Your BMI is: {bmi}")
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
    else:
        print(bmi)
except ValueError:
    print("Invalid input! Please enter numerical values.")