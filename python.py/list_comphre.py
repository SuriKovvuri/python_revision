'''
List Comprehension:
List comprehension is a concise way to create lists in Python. It allows you to generate a new list by performing an operation on each item in an existing iterable (like a list, tuple, or range), optionally filtering elements with a condition — all in a single line of code.

Syntax:
new_list = [expression for item in iterable if condition]


why we are using:
List comprehension makes code shorter, faster, and more readable, especially when you're working with data transformations or filtering.
'''
# Creating a List
numbers = [x for x in range(5)]
print(numbers)  # Output: [0, 1, 2, 3, 4]

squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]


'''
# List Comprehension with Conditions
'''
fruits = ["apple", "banana", "grapes", "Guava", "mango"]
fruits_list = [fruit for fruit in fruits if 'apple' in fruit]
print(fruits_list) #output: ['apple']


evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]


#List Comprehension with if-else (Conditional Expression)
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # Output: ['even', 'odd', 'even', 'odd', 'even']     