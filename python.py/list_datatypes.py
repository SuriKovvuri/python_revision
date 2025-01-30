'''
integer
string
float
complex
None
Boolean
'''

x = 7
print(type(x));
print(x)

y = "suri"
print(type(y))
print(y)

z = True
print(type(z))
print(z)


#Array
my_list = ["apple", "banana", "cherry"]
print(my_list)

#mixed array
mixed = [1, "apple", 3.14, True]
print(mixed)

#Find Index
print(my_list[0])
print(mixed[1])
print(my_list[-1])
print(my_list[-2])

#Modifying elements (Modifying the existing elements)
my_list[1] = "mango"
print(my_list)

#Append(): Add single element to the end of the list
my_list.append("strawberry")
print(my_list)    

#insert(): Insert a single elemet at specific index
my_list.insert(1,"lemon")
print(my_list)

#extend(): Adds multiple elements (another list or any iterable) to the end of the list.
my_list.extend(["carrot", "beetroot"])
print(my_list)

#Remove(): Removes the first occurrence of an element.
my_list.remove("strawberry")
print(my_list)

#pop(): Removes an element by index (and returns it). If no index is specified, it removes the last item.
my_list.pop(2)
print(my_list)

#clear(): Removes all elements from the list.
my_list.clear();
print(my_list)





#List Operations
#Slicing: You can retrieve a subset of the list using slicing
numbers = [1,2,3,4,5,6]
slice = numbers[2:4]
print(slice)

#Length : Length of List
length = len(numbers)
print("lenth is ", length)

#Concatinate
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)

print(4 in list3)

#using for loop
fruits = ["apple", "banana", "strawberry", "mango"]
for fruit in fruits:
    print(fruit)

vegetable = ["carrot", "beetroot", "califlower", "cabbage"]
for vegetables in vegetable:
    print(vegetables)


#List Methods
#sort(): xSorts the list in ascending order.
marks = [1,5,2,8,2]
marks.sort()
print(marks)
#reverse();
marks.reverse()
print(marks)

#index(): Returns the index of the first occurrence of a specified element.
ind = marks.index(5)
print(ind)
