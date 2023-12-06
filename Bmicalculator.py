def calculate_bmi(weight, height):
    # BMI formula: weight / (height^2)
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")

    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Interpret BMI
    interpretation = interpret_bmi(bmi)

    # Display the results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are categorized as: {interpretation}")

if __name__ == "__main__":
    main()
