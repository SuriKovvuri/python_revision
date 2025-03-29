'''
Lambda Function: Python's lambda functions are small anonymous functions as they do not have a name and are contained in a single line of code.

syntax:
lambda arguments: expression

Example:
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8


lambda function using:
map()	Applies a function to each item in an iterable and returns a new iterable.
filter()	Selects elements from an iterable based on a condition (returns only True values).
reduce()	Applies a function cumulatively to reduce an iterable into a single value.
'''

'''
with map() : Transforming Data
Applies a function to each element and returns a new iterable.
Returns a map object, which can be converted to a list.
'''
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # Output: [1, 4, 9, 16]

'''
with filter(): Selecting Specific Elements based on condition
               Keeps only elements that satisfy a condition.
               Returns a filter object, which can be converted to a list.
'''
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4]


'''
with reduce(): Combining All Elements
'''
from functools import reduce
numbers = [1, 2, 3, 4, 5]
# Using reduce() to multiply all elements
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

