"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.


"""
filename = 'output.txt'
try:
    # Reading first — this will raise FileNotFoundError if file doesn't exist
    with open(filename, 'rt') as fh:
        pass

    text = input("Enter text to write to the file: ")
    with open(filename, 'wt') as fh:
        fh.write(text)
    print(f'\nData successfully written to {filename}')
    text2 = input("Enter additional text to append: ")

    with open(filename, 'at') as fh:
        fh.write('\n' + text2)
        print('\nData successfully appended')

    with open(filename,'rt') as fh:
        content = fh.read()
    print(f'\nFinal content of {filename}')
    print(content)

except FileNotFoundError:
    print('File not found')
except Exception as e:
    print(e)




