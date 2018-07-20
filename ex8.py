formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "In Xanadu did Kubla Khan\n",
    "A stately pleasure-dome decree:\n",
    "Where Alph, the sacred river, ran\n",
    "Through caverns measureless to man\nDown to a sunless sea."
))
