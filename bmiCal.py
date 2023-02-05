# BMI Calculator Program


def calculate_bmi():
    # Input height in centimeters
    height = input("Height in centimeters: ")

    # Input weight in kilograms
    weight = input("Weight in kilograms: ")

    # Try converting input to float and calculate BMI
    try:
        height = float(height)
        weight = float(weight)

        # Convert height from centimeters to meters
        height = height / 100

        # Calculate Body Mass Index (BMI)
        bmi = weight / (height * height)

        # Display the calculated BMI rounded to 2 decimal places
        print("Your BMI is: {:.2f}".format(bmi))

    # In case of invalid input
    except:
        print("Please enter a valid number.")


# Run the program if it is the main module
if __name__ == '__main__':
    calculate_bmi()
