# "end = ' '" tells print not to end the line with /n
print("How old are you? (only input number, in years)", end = ' ')
age = input()
print("How all are you? (only input number, in centimeters)", end = ' ')
height = float(input())/100
print("How much do you weigh? (only input number, in kilograms)", end = ' ')
weight = float(input())

BMI = round(weight/(height**2),2)

print(f"So, you're {age} years old, {height} m tall and {weight} kg heavy.")
print(f"Your Body Mass Index is {BMI}. See if it is in range 19.0 to 25.0.")
