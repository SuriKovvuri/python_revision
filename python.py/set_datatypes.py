#Sets: In Python, a set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements, but each element must be hashable (like numbers, strings, and tuples).

#Method	            Description
#add()	            Adds an element to the set
#remove()	        Removes a specific element (raises KeyError if not found)
#discard()	        Removes a specific element (no error if not found)
#pop()	            Removes and returns an arbitrary element
#clear()	        Removes all elements from the set
#union()	        Returns the union of two sets
#intersection()	    Returns the intersection of two sets
#difference()	    Returns the difference between two sets
#symmetric_difference()	Returns the symmetric difference between two sets
#update()	        Adds all elements from another set
#issubset()	        Checks if one set is a subset of another
#issuperset()	    Checks if one set is a superset of another

#Use Cases of Sets:
#Removing duplicates: Since sets automatically discard duplicates, they are ideal for deduplicating lists or sequences.
#Membership testing: Checking if an element exists in a set is very efficient (O(1) average time complexity).
#Mathematical operations: Sets are useful for performing operations like union, intersection, and difference on groups of data.
#Summary:
#Sets are unordered collections of unique elements in Python.
#They are useful for eliminating duplicates, performing set operations, and checking membership.
#Sets provide a range of built-in methods for adding, removing, and manipulating data.

# Creating a set with curly braces
my_set = {1,2,3,4,5}
print(my_set)
# Creating a set with the set() constructor
another_set = set([3,4,5,6,7,8])
print(another_set)
# Empty set (You must use the set() function, {} creates an empty dictionary)
empty_set = set()
print(empty_set)


#Adding Elements to a Set using add() method
#add():
my_set.add(6)
print(my_set)

#Removing Elements from a Set using : remove(), discard(), pop()
my_set.remove(6)
print(my_set)
my_set.discard(5)
print(my_set)
removed_element =my_set.pop()
print(removed_element)
print(my_set)

#Set Union, Intersection, and Difference
set1 = {1,2,3,4}
set2 = {4,5,6,7}
union_set = set1.union(set2)
print(union_set)
intresection_set = set1.intersection(set2)
print(intresection_set)
difference_set = set1.difference(set2)
print(difference_set)
symetric_difference_set = set1.symmetric_difference(set2)
print(symetric_difference_set)


# Checking for Membership:
print(4 in set1)


#set length
print(len(set1))

#clear(): clear the set
set1.clear()
print(set1)



#Example: Removing Duplicates from a List Using a Set
my_list = [1, 2, 3, 1, 2, 4, 5]
my_seta = set(my_list)
print(my_list)
print(my_seta)
unique_list = set(my_seta)
print(unique_list)
