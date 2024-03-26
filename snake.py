import re

input_str = input("Check the movement of the snake: ")

if len(input_str) == 7:
    pattern = re.compile(r'ff|ll')
    matches = pattern.findall(input_str)

    if matches:
        print("Pattern found in the input string.")
        for match in matches:
            print(match)
    else:
        print("Pattern not found in the input string.")