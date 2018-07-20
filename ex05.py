# Create some string
name = "Zhen"
age = 18
height = 170.0 # cm
weight = 62.0 # kg
eyes = "brown"
teeth = "white"
hair = "black"

height_inch = round(height * 0.393700787, 1)
weight_lbs = round(weight * 2.20462262185, 1)

# Print. "f" at start means things inside {} need to be formatted.
print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall, i.e. {height_inch} inches.")
print(f"He's {weight} kilograms heavy, i.e. {weight_lbs} pounds.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
