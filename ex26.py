# Download file from command line
# wget -o ex26.py http://learnpythonthehardway.org/python3/exercise26.txt

# RUN
# python ex26.py test.txt

# Below this line, comments are original and corrected are below one line.

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
# NAN
height = input()
# print("How much do you weigh?", end=' '
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# NAN
from sys import argv
script, filename = argv

# txt = open(filenme)
txt = open(filename)

# print("Here's your file {filename}:")
print(f"Here's your file {filename}:")
# print(tx.read())
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

# print(txt_again_read())
print(txt_again.read())

# print('Let's practice everything.')
print('Let\'s practice everything.')
# print('You\'d need to know \'bout escapes
#       with \\ that do \n newlines and \t tabs.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# print("--------------)
print("--------------")
print(poem)
# print(--------------")
print("--------------")

# five = 10 - 2 + 3 -
five = 10 - 2 + 3 - 6
# print(f"This should be five: {five}"
print(f"This should be five: {five}")

# def secret_formula(started)
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
#     crates = jars  100
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
# beans, jars = secret_formula(start_point)
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
# formula = secret_formula(startpoint)
formula = secret_formula(start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
# cates = 30
cats = 30
dogs = 15


if people < cats:
#    print "Too many cats! The world is doomed!"
    print("Too many cats! The world is doomed!")

# if people < cats:
if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

# if people > dogs
if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

# if people <= dogs
if people <= dogs:
#     print("People are less than or equal to dogs.)
    print("People are less than or equal to dogs.")


# if people = dogs:
if people == dogs:
    print("People are dogs.")
