# # list
# #Ordered # Mutable #Allow Duplicates #Hetrogenous
# #Ordered and mutable collection of elements


# # a = [1,2,3,"Apple",True]
# # print(type(a))

# # #adding : #append, #insert #extend
# # #append
# # a.append("Babu")
# # print(a)

# # a.insert(2,4)
# # print(a)

# # a.extend([5,6])
# # print(a)



# # #Delete
# # #remove() #pop() clear()
# # c = [1,2,3,"Suei","Babu", "kovvuri"]
# # print(c)
# # c.remove(1)
# # print(c)
# # c.remove("Suei")
# # print(c)
# # c.pop()
# # print(c)
# # c.clear()
# # print(c)




# # #Sort #reverse(), sort()
# # b = [2,3,4,5,6,7,8,1]
# # print(b)
# # b.reverse()
# # print(b)
# # b.sort()
# # print(b)


# #search
# #index(), #count
# d = [1,2,2,3,3,4,5,6,7]
# print(d)
# print(d[0])
# print(d[4])

# d[-1] = "Suri"
# print(d)
# d[0] = 0
# print(d)


# ss = d.count(2)
# print(ss)
# ss = d.count(3)
# print(ss)


# #Copy
# f = [1,2,4]
# print(f)
# c = f.copy()
# print(c)


# #Oprrations
# #indexing #Slicing  #Concatination #Repetition #Membership #iteration #length #list #list_compreshension

# #indexing 
# a = [1,2,4]
# print(a[0])
# print(a[1])
# print(a[-1])


# a = [1,2,3,4,5,6,7,8]
# slice = a[2:5]
# print(slice)
# print(a[4:-2])

# #concatenation
# a = [1,2,3,4]
# b = ["Suri", "Babu", "Kovvuri"]
# c = a + b
# print(c)

# rep = b * 3
# print(rep)

# length = len(a)
# print(length)

# ss = ["Suri","Babu","Kovvuri","Sita","Srinu"]
# for i in ss:
#     print(i)
    
# dd = [x**2 for x in range(5)]
# print(dd)
# dd1 = [x for x in range(10) if x % 2 ==0]
# print(dd1)




# #Tuple
# #Ordered #immutable #Donot Allow the duplicates
# #Indexing
# a = (1,2,4,5)
# print(a.index(1))
# print(a[0])

# #count
# b = (1,2,3,5,6)
# print(b.count(1))

# #Repetition
# c = b * 3
# print(c)

# a = (1,2,3,4,5)
# b = (5,6,7,8,9,0)
# c = a + b
# print(c)

# print(1 in a)
# print(10 in a)

# print(len(a))

# slice = (1,2,3,4,2,3,1,4,6)
# print(slice[2:7])


# tuple = 1, "Suri", True
# print(tuple)

# a , b, c = tuple
# print(a)
# print(b)
# print(c)




# #dictionary
# my_dict = {"name":"suri",
#            "age":24,
#            "boolean": True
#            }
# print(my_dict)

# #Accessing
# print(my_dict["name"])

# #adding
# my_dict["gender"] = "Male"
# print(my_dict)

# #removing
# #pop() #del #clear()
# #pop()
# my_dict.pop("boolean")
# print(my_dict)

# #del
# del my_dict["gender"]
# print(my_dict)

# #clear()
# my_dict.clear()
# print(my_dict)


# student = {"name":"suri",
#            "age":25,
#            "gender":"Male",
#            "is_married":"No"
#            }
# for key in student.keys():
#     print(key)
    
# for val in student.values():
#     print(val)
    
# for key,val in student.items():
#     print(f"{key}:{val}")
    
    
# squares = {x:x**2 for x in range(5)}
# print(squares)





# #sets
# #unordered mutable collection of elements
# my_set = {1,2,3,4,5,6,7}
# #add
# print(my_set)
# my_set.add(8)
# print(my_set)
# my_set.add(9)
# print(my_set)

# #REemoving
# #discard(), #pop() #remove()
# a = {1,2,4,5,6,7,8}
# a.remove(1)
# print(a)

# a.pop()
# print(a)

# a.discard(8)
# print(a)

# a.clear()
# print(a)

# c = {1,2,3,4,5,6,7}
# d = {5,6,7,8,9,0}
# union = c.union(d)
# print(union)
# intrse = c.intersection(d)
# print(intrse)
# diff = c.difference(d)
# print(diff)
# diffe = d.difference(c)
# print(diffe)


# empty_list = list((1,2,4))
# print(empty_list)
# list_con = list((1,2,4))
# print(list_con)


# empty_set = set()
# print(empty_set)
# set_con = set((1,2,4))
# print(set_con)


# empty_dict = dict()
# print(empty_dict)
# dict_con = dict({"name":"suri"})
# print(dict_con)

# empty_tuple = tuple()
# print(empty_tuple)





import csv
rows = [
    ["Name","Age","Gender"],
    ["Suri",25,"Male"],
    ["Babu",24,"Male"],
    ["Kovvuri",23,"Male"]
]

with open("new.csv", mode="w", newline='') as file:
    file = csv.writer(file)
    file.writerows(rows)
    
    


