# This is a program developed to calculate a person's Body Mass Index (BMI)
# Users are required to provide their body's weight in kilograms and height in metres.

users_weight = input("Enter your weight in kilograms: ")

users_height = input("Enter your height in metres: ")

# Calculate User's bmi
users_bmi = users_weight / users_height**2

print(users_bmi)
