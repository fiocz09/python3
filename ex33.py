# while-loop
"""
numbers = []

def append_numbers_while(var, inc):
    i = 0

    while i < var:
        # print(f"At the top i is {i}.")
        numbers.append(i)

        i += inc
        # print("Numbers now: ", numbers)

        # print(f"At the bottom i is {i}.")

    return numbers

append_numbers_while(7, 2)
print("The numbers: ")
for num in numbers:
    print(num)
"""

# for-loop
numbers = []

def append_numbers_for(var, inc):
    for i in range(0, var, inc):
        numbers.append(i)
        print(f"I now: {i}.")
        print(f"Numbers now: ", numbers)
    return numbers

append_numbers_for(7, 2)
print("The numbers: ")
for num in numbers:
    print(num)
