#Single inheritance:

# Test: Single-Level Inheritance
# Problem Statement:
# Create a parent class Vehicle with the following:

# An __init__ method that initializes the attributes brand and model.
# A method vehicle_info() that prints: "Vehicle Brand: <brand>, Model: <model>".
# Create a child class Car that inherits from Vehicle and adds the following:

# An additional attribute fuel_type in its __init__ method.
# A method car_info() that prints: "This car uses <fuel_type> as fuel.".

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def vehicle_info(self):
        print(f"Vehicle Brand: {self.brand}, Model: {self.model}")
        
class Car(Vehicle):
    def __init__(self, brand, model,fuel_type):
        self.fuel_type = fuel_type
        super().__init__(brand, model)
    def car_info(self):
        print(f"This car uses {self.fuel_type} as fuel.")
        

obj = Car(brand="TATA",model="TIGOR",fuel_type="Petrol")
obj.vehicle_info()
obj.car_info()











# #inheritance
# class A:
#     def __init__(self):
#         print("Initilize the data...")
#     def greet(self):
#         print("Hi this is Babu")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Derived class")
#     def wish(self):
#         print("Welcome")
# obj = B()
# obj.greet()
# obj.wish()



#Multi-level inheritance

# Multi_level inheritance:
    
class A:
    def method_a(self):
        print("A data is")
class B(A):
    def method_b(self):
        print("B data is")
class C(B):
    def method_c(self):
        print("C data is")
obj = C()
obj.method_a()
obj.method_b()
obj.method_c()


# Base class (Grandparent)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived class (Parent)
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Calling the constructor of the base class
        self.grade = grade
    
    def student_info(self):
        print(f"Grade: {self.grade}")

# Derived class (Child)
class Scholar(Student):
    def __init__(self, name, age, grade, scholarship_amount):
        super().__init__(name, age, grade)  # Calling the constructor of the Student class
        self.scholarship_amount = scholarship_amount
    
    def scholarship_info(self):
        print(f"Scholarship Amount: {self.scholarship_amount}")


# Creating an object of the Grandchild (Scholar) class
student1 = Scholar("Alice", 20, "A", 1000)

# Calling methods from all levels of inheritance
student1.info()              # From Person class
student1.student_info()      # From Student class
student1.scholarship_info()  # From Scholar class



# 2nd example
# Create two base classes:
# Person: This class should have the following attributes:
# name (string)
# age (integer)
# A method display_info() that prints: "Name: <name>, Age: <age>".
# Employee: This class should have the following attribute:
# employee_id (string)
# A method display_employee() that prints: "Employee ID: <employee_id>".
# Create a derived class Manager:
# Inherit from both Person and Employee classes.
# Add the following attribute to the Manager class:
# department (string)
# Add the method display_manager() that prints: "Department: <department>".
# Create an object of the Manager class and display:
# Information about the person (from Person class).
# Employee details (from Employee class).
# Manager-specific details (from Manager class).

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
        
class Employee(Person):
    def __init__(self, name, age,employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")
        
        
class Manager(Employee):
    def __init__(self, name, age, employee_id,department):
        super().__init__(name, age, employee_id)
        self.department  = department 
        
    def display_manager(self):
        print(f"Department: {self.department}")


obj = Manager("suri",25,"101","cse")
obj.display_info()
obj.display_employee()
obj.display_manager()





#======================= #Hierarchy=====================

# class A:
#     def aa(self):
#         print("AAAA")
# class B(A):
#     def bb(self):
#         print("BBBB")
# class C(A):
#     def cc(self):
#         print("CCCc")

# obj = C()
# obj.aa()
# obj.cc()

# obj1 = B()
# obj1.bb()
# obj1.aa()





# Base Class Animal:

# Create an Animal class with the following attributes and method:
# name (string)
# age (integer)
# A method display_info() that prints: "Name: <name>, Age: <age>".
# Derived Class Mammal:

# Create a Mammal class that inherits from Animal.
# Add an additional attribute habitat (string).
# Add a method mammal_info() that prints: "Habitat: <habitat>".
# Derived Class Dog:

# Create a Dog class that inherits from Mammal.
# Add an additional attribute breed (string).
# Add a method dog_info() that prints: "Breed: <breed>".
# Create an Object of Dog:

# Create an object of the Dog class and display:
# Information about the animal (from Animal class).
# Information about the mammal (from Mammal class).
# Information about the dog (from Dog class).

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
class Mammal(Animal):
    def __init__(self, name, age,habitat):
        super().__init__(name, age)
        self.habitat = habitat
    def mammal_info(self):
        print(f"Habitat: {self.habitat}")


class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed
    
    def dog_info(self):
        print(f"Breed: {self.breed}")
        
obj = Dog(name="Puppy",age=7,breed="german shepord")
obj.display_info()
obj.dog_info()

obj1 = Mammal(habitat='habitats',age=8,name="Alice")
obj1.display_info()
obj1.mammal_info()













# ===================Multiple======================
class A:
    def aa(self):
        print("AAAAA")
class B():
    def bb(self):
        print("BBBBB")
class C(A,B):
    def cc(self):
        print("CCCCC")
obj = C()
obj.aa()
obj.bb()
obj.cc()



# Base Class 1: Person
# Attributes:
# name (string)
# age (integer)
# Method:
# display_person_info() that prints: "Name: <name>, Age: <age>".
# Base Class 2: Employee
# Attributes:
# employee_id (string)
# department (string)
# Method:
# display_employee_info() that prints: "Employee ID: <employee_id>, Department: <department>".
# Derived Class: Manager
# The Manager class should inherit from both Person and Employee classes.
# Additional Attribute:
# office_location (string)
# Method:
# display_manager_info() that prints: "Office Location: <office_location>".

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        

class Employee:
    def __init__(self,employee_id,department):
        self.employee_id = employee_id
        self.department = department
    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")
        

class Manager(Person,Employee):
    def __init__(self, name, age,office_location,employee_id,department):
        Person.__init__(self,name, age)
        Employee.__init__(self,employee_id,department)
        self.office_location = office_location
    def display_manager_info(self):
        print(f"Office Location: {self.office_location}")

obj = Manager(office_location="Chennai",age=25,name="suri",department="cse",employee_id="101")
obj.display_person_info()
obj.display_employee_info()
obj.display_manager_info()


# Example2:
# Base Class 1: Vehicle
# Attributes:
# brand (string)
# model (string)
# Method:
# display_vehicle_info() that prints: "Brand: <brand>, Model: <model>"
# Base Class 2: Engine
# Attributes:
# engine_type (string)
# horsepower (integer)
# Method:
# display_engine_info() that prints: "Engine Type: <engine_type>, Horsepower: <horsepower>"
# Derived Class: Car
# Inherit from both Vehicle and Engine.
# Additional Attribute:
# color (string)
# Method:
# display_car_info() that prints: "Color: <color>"


class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display_vehicle_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Engine:
    def __init__(self,engine_type,horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower
    def display_engine_info(self):
        print(f"Engine Type: {self.engine_type}, Horsepower: {self.horsepower}")

class Car(Vehicle,Engine):
    def __init__(self, brand, model,color,engine_type,horsepower):
        Vehicle.__init__(self,brand, model)
        Engine.__init__(self,engine_type,horsepower)
        self.color = color
    def display_car_info(self):
        print(f"Color: {self.color}") 

obj = Car(brand="TATA",color="Blue",engine_type="BS4",horsepower=1200,model="2024")
obj.display_vehicle_info()
obj.display_engine_info()
obj.display_car_info()





# ==================Hybrid Inheritance==================
# Base Class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")

class Manager(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department
    def display_manager_info(self):
        print(f"Department: {self.department}")

class Director(Manager, Employee):
    def __init__(self, name, age, employee_id, department, office_location):
        super().__init__(name, age, employee_id, department)
        self.office_location = office_location
    def display_director_info(self):
        print(f"Office Location: {self.office_location}")


# Testing the classes
director = Director("John Doe", 45, "D123", "Sales", "Headquarters")
director.display_person_info()  # From Person class
director.display_employee_info()  # From Employee class
director.display_manager_info()  # From Manager class
director.display_director_info()  # From Director class
