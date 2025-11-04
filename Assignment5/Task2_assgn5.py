"""
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list


"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#task1
list2 = list1[0:5]


#task2
list3 = list2[::-1]
print(f'Original list: {list1}')
print(f'Extracted first five elements : {list2}')
print(f'Reversed extracted elements: {list3}')