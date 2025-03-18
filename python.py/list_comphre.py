# Creating a List
numbers = [x for x in range(5)]
print(numbers)  # Output: [0, 1, 2, 3, 4]


squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]


# List Comprehension with Conditions
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Using if-else Inside  
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)  # Output: ['even', 'odd', 'even', 'odd', 'even']     