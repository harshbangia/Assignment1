"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""


file_name = 'sample.txt'
try:
    with open(file_name, 'w') as fh:
        line_number = 1
        for line in fh:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1

except FileNotFoundError as file_err:
    print(f'Error: The was not {file_name} found.')
    print(file_err)

except Exception as e:
        print(f"An unexpected error occurred: {e}")
