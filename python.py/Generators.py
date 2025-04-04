'''
A generator in Python is a special type of iterator that allows you to generate values one at a time using the yield keyword, instead of returning all values at once like a list. 
They are memory-efficient and useful when working with large datasets or streams of data.


Key Concepts:

Uses yield instead of return
Produces values lazily (on-the-fly, only when needed)
Saves memory (doesn't store the entire list in memory)
A generator is a function that automatically creates an iterator.


Advantages:

Memory-efficient : Doesn't load the entire file into RAM.
Faster Execution for large files : Only processes one row at a time.
Handles large datasets smoothly.


✅ 2 Main Reasons Why We Use Generators in Python

1️⃣ Memory Efficient (Saves RAM)
Generators don’t store all values in memory. (Saves Memory)
They generate values one at a time, only when needed.
2️⃣ Faster for Streaming / Large Data
Generators are ideal when you're working with large files, logs, or live data streams.
'''

#Basic: 
def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3



def generate_evens(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i
limit = 10

# gen = generate_evens(limit)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for num in generate_evens(limit):
    print(num)





'''
✅ Definition of yield:
The **yield** keyword is used inside a function to turn it into a generator.
Instead of returning a single value and ending the function (like return), yield pauses the function, sends back a value, and resumes from where it left off the next time it’s called.

🧠 Think of yield as:
"Give me a value now, and I’ll come back later for the next one."
'''

import csv

with open('large_sample_data.csv', mode='r')as file:
    read = csv.reader(file)
    
    for line in read:
        print(line)
        



import csv

def read_large_csv(filename = 'large_sample_data.csv'):
    """Generator function to read a large CSV file line by line."""
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row (optional)
        for row in reader:
            yield row  # Yield one row at a time

# Usage of the generator
for line in read_large_csv('large_sample_data.csv'):
    print(line)  # Process each row (prints one row at a time)


'''
Generators are a type of iterable in Python that allow you to iterate over data without storing it all in memory at once. They are useful for handling large datasets or infinite sequences efficiently.
Generators are widely used to handle large datasets, databases, and file systems efficiently. Since they generate data on the fly instead of loading everything into memory, they are perfect for scenarios where handling large amounts of data at once would be too memory-intensive.

It uses a generator (yield) to return one row at a time instead of storing everything in memory.



Key Differences:

Feature	                Without Generator (Direct File Read)	With Generator (yield Function)
Memory Usage	        Loads entire file into memory	        Reads and processes one row at a time
Efficiency	            Slower for large files	                Faster as it processes only what is needed
Flexibility	            Harder to extend and reuse	            Can be reused and modified easily
Control over Data	    Cannot pause/resume iteration	        Can pause and resume iteration
Handles Large Files	    Might crash for very large files	    Works smoothly even for huge files


Differences:

Feature	Lists	    Generators
Memory Usage	    High (stores all data)	    Low (stores only one item at a time)
Speed	            Slower for large data	    Faster due to lazy evaluation
Use Case	        Small datasets	            Large datasets, files, DBs
'''
