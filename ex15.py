from sys import argv

script, filename = argv

# open the file
txt = open(filename)

print(f"Here's your file {filename}:")
# read the file just opened. give file a command using "read" after "."
print(txt.read())

txt.close()

#print("Type the filename again:")
#file_again = input("> ")
#
#txt_again = open(file_again)
#
#print(txt_again.read())
#
#txt_again.close()
