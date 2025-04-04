import copy

orginal_list = [[1,2,3],[4,5,6]]

copy_list = copy.deepcopy(orginal_list)

copy_list[0][0] = 99

print(orginal_list)
print(copy_list)

'''
1. copy.copy() (Shallow Copy)
Creates a new object but does not create copies of nested objects.
If the original object contains other objects (like lists inside lists), the references to those objects are copied instead of the actual objects.
Modifications to nested objects will affect both the original and the copied object.

import copy
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original_list)
# Modifying the nested list
shallow_copy[0][0] = 99
print(original_list)  # [[99, 2, 3], [4, 5, 6]] (Changed)
print(shallow_copy)   # [[99, 2, 3], [4, 5, 6]] (Same as original)


2. copy.deepcopy() (Deep Copy)
Creates a new object and recursively copies all nested objects.
The new object is completely independent of the original object.
Modifications to nested objects will not affect the original object.

import copy
original_list = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(original_list)
# Modifying the nested list
deep_copy[0][0] = 99
print(original_list)  # [[1, 2, 3], [4, 5, 6]] (Unchanged)
print(deep_copy)      # [[99, 2, 3], [4, 5, 6]] (Only deep copy is changed)


When to Use Which?
✅ Use copy.copy() if your object is simple (like a list of integers or strings).
✅ Use copy.deepcopy() if your object contains nested mutable objects (like lists inside lists, dictionaries with lists, etc.).

Key Differences Summary:
Feature	                    copy.copy() (Shallow Copy)	                  copy.deepcopy() (Deep Copy)
Copies Object	            ✅ Yes	                                    ✅ Yes
Copies Nested Objects	    ❌ No (References remain)	                ✅ Yes (New objects created)
Changes Affect Original?	✅ Yes (For nested objects)	                ❌ No (Completely independent)
Use Case	                When object is simple (no nested structures)  When object contains nested lists, dicts, etc.


Understanding copy_list[i][j] Notation

orginal_list = [
    [1, 2, 3],  # Row 0
    [4, 5, 6]   # Row 1
]
# Each element in original_list is itself a list, meaning it's a list of lists (2D list).

copy_list[0] → Refers to the first sub-list [1, 2, 3]
copy_list[1] → Refers to the second sub-list [4, 5, 6]
copy_list[0][0] → First element of the first sub-list → 1
copy_list[0][1] → Second element of the first sub-list → 2
'''