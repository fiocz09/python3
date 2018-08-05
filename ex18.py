# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# OK, that *args is actually pointless, we can just do This
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no argument
def print_none():
    print("I got nothin'.")

print_two("Cao", "Zhen")
print_two_again("Cao", "Zhen")
print_one("First!")
print_none()
