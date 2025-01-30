# Types of Comprehensions
    # List Comprehensions
    # Set Comprehensions
    # Dictionary Comprehensions
    
#List Comprehensions

# [expression for item in iterable if condition]

square = [x**2 for x in range(10) if x%2==0]
print(square)

a = [20,30,40,50]
plus_one = [x + 1 for x in a if x % 2 == 0]

print(plus_one)


#  Set Comprehensions
# A set comprehension is similar to a list comprehension, but it creates a set, which stores unique values.

# Syntax:
# {expression for item in iterable if condition}

square = {x**2 for x in range(10) if x%2==0}
print(square)

c = [10,20,30,40]
plus_one = {x+1 for x in c if x%2==0}
print(plus_one) 


#Dictionary Comprehensions
# A dictionary comprehension is used to create a dictionary from an iterable.

# Syntax:
# {key_expression: value_expression for item in iterable if condition}

square = {x: x**2 for x in range(10)}
print(square)


# Swap keys and values in a dictionary:

original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # Output: {1: 'a', 2: 'b', 3: 'c'}

# Filter dictionary items:
squares_dict = {x: x**2 for x in range(5)}
filtered_dict = {k: v for k, v in squares_dict.items() if v > 5}
print(filtered_dict)  # Output: {3: 9, 4: 16}

