#Tuple:A tuple is an ordered, immutable collection of items in Python. Tuples are similar to lists, but unlike lists, they cannot be modified after creation (i.e., you can't change, add, or remove elements). Tuples are defined by placing the elements inside parentheses () and separated by commas.
#Key Features of Python Tuples:
#Ordered: Tuples maintain the order of elements as they were inserted.
#Immutable: Once created, elements inside a tuple cannot be changed, added, or removed.
#Heterogeneous: A tuple can store elements of different data types (e.g., integers, strings, floats).
#Indexable: You can access elements in a tuple using their index (starting from 0).
#Allows Duplicates: Unlike sets, tuples allow multiple instances of the same element.
#Faster than lists: Due to immutability, tuples are more memory-efficient and faster than lists.


numbers = (1,2,3,4,5,2,3,4)
print(numbers)
mixed = (1, "suri", True)
print(mixed)

#Accessing tuple elements
#Using index
fruits = ("apple", "mango", "orange")
print(fruits[0])
print(fruits[1])
print(fruits[-1])

#Tuple is immutable
#fruits[1] = "strawberry"
#print(fruits)

#Count(): Returns the number of times a specified element appears in the tuple.
print(numbers.count(2))
print(numbers.count(3))

#index(): Returns the index of the first occurrence of a specified element.
print(numbers.index(2))
print(numbers.index(5))

#Concatenation: You can concatenate two or more tuples using the + operator.
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
print(tuple3)

#slicing:
fetch = numbers[1:5]
print(fetch)

#length
print(len(numbers))


#Repetetion:
vegetables = ("carrot", "beetroot")
repeated = vegetables * 3;
print(repeated)


#Membership test
print("carrot" in vegetables)



#Touple packing and unpacking
#packed touple

packed_tuple = 1,2,"suri"
print(packed_tuple)


#Unpaked tuple

unpacked_tuple = (1, 2, "suri")
a,b,c = unpacked_tuple
print(a)
print(b)
print(c)
