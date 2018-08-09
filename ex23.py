# Download file from command line
# wget -o languages.txt https://learnpythonthehardway.org/python3/languages.txt

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    # Read one line from file(pre-opened)
    line = language_file.readline()
    # if-statement, print one line and another
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    # Strip \n at end of each line
    next_lang = line.strip()
    # Decode bytes, encode strings.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")
main(languages, input_encoding, error)

# COMMAND LINE
# ex23.py utf-8 strict
