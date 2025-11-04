"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""

student_info = {'Harsh':95,
                'Alice':58,
                'Bob':82,
                'Jim':75,
                'Joe':65,
                'Anjali':44,
                'Ali':00}

name = input('Enter the student\'s name: ')

if name in student_info.keys():
    print(f'{name}\'s marks: {student_info[name]}')
else:
    print('Student not found')