#In Python, a dictionary is an unordered, mutable collection that holds key-value pairs. 
#Each key in the dictionary is unique, and it maps to a specific value.

#Creating a dictionary

#Empty Dictionary
my_dict ={}
print(my_dict)

# Dictionary with mixed data types for values
student = {
        'name':'suri',
        'age' : 24,
        'is_employee' : True
        }
print(student)

#Accessing the Dictionary values
print(student['name'])
print(student['is_employee'])
print(student.get("name"))
print(student.get("age"))


#Adding or Updating a key-value pair
student["gender"] = "Male"
student["job"] = "software"
print(student)


#Removing key-value pair
#pop(): Removes a key-value pair and returns the value
job = student.pop("job")
print(job)
print(student)
#using delete operator
del student["gender"]
print(student)

#clear():
student.clear();
print(student)




#Looping Through a Dictionary
cars = {
        'name' : 'Tigor',
        'brand' : 'Tata',
        'owner' : 'suri',
        'color' : 'white'
        }
#Loop through keys:
for key in cars:
    print(key)
#Loop through values:
for value in cars.values():
    print(value)
#Loop through key-value pairs:
for key, value in cars.items():
    print(f"{key} : {value}")


#Dictionary_methods:
#keys(),values(),items()
print(cars.keys())
print(cars.values())
print(cars.items())
#update():
cars.update({'is_good' : True})
print(cars)
#pop(): removes the key-value pair using key
isgood = cars.pop("is_good")
print(cars)


#Checking if a Key Exists:
if "name" in cars:
    print("The 'name' key exists.")



#Nested Dictionaries:
# Nested dictionary representing students and their subjects with grades
school_data = {
    "class1": {
        "student1": {
            "name": "Alice",
            "age": 25,
            "subjects": {
                "Math": 90,
                "Science": 85,
                "English": 88
            }
        },
        "student2": {
            "name": "Bob",
            "age": 24,
            "subjects": {
                "Math": 78,
                "Science": 80,
                "History": 89
            }
        }
    },
    "class2": {
        "student1": {
            "name": "Charlie",
            "age": 22,
            "subjects": {
                "Math": 92,
                "Geography": 75,
                "English": 80
            }
        },
        "student2": {
            "name": "David",
            "age": 23,
            "subjects": {
                "Math": 85,
                "Science": 90,
                "Art": 95
            }
        }
    }
}
print(school_data["class1"]["student1"]["name"])
print(school_data["class2"]["student2"]["subjects"]["Math"])


nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# print(nested_dict)


for key, inner_dict in nested_dict.items():
    print(f"keys{key}")
    print(f"innner_dict{inner_dict}")
    print(f"{key}:{inner_dict}")
    
    for key , val in inner_dict.items():
        print(f"{key}:{val}")
    