# This is a program developed to calculate a person's Body Mass Index (BMI)
# Users are required to provide their body's weight in kilograms and height in metres.

weight = input("Enter your weight in kilograms: ")

height = input("Enter your height in metres: ")

# Calculate User's bmi
bmi = weight / height**2

print(bmi)
