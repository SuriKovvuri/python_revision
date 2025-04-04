# Class: Car is the class, which is the blueprint for creating car objects.
# Object: bmw is an object (instance) of the Car class.
# Attributes:
# "Black" is the color of the car.
# "1500 kg" is the weight of the car.
# "250 km/h" is the speed of the car.
# "BMW X5" is the model of the car.


# Define the Car class
class Car:
    # Constructor to initialize the common features (attributes)
    def __init__(self, color, weight, speed, model):
        self.color = color
        print(self.color)
        self.weight = weight
        self.speed = speed
        self.model = model
    
    # Define the common functionalities (methods)
    def startCar(self):
        print(f"The {self.model} is starting.")
    
    def changeGear(self, gear):
        print(f"The {self.model} is changing to gear {gear}.")
    
    def slowDown(self):
        print(f"The {self.model} is slowing down.")
    
    def brake(self):
        print(f"The {self.model} is braking.")

# Create an object (instance) of the Car class
BMW = Car("Black", "1500 kg", "250 km/h", "BMW X5")

# Access the object's data members (attributes)
print(f"BMW Details: Color: {BMW.color}, Weight: {BMW.weight}, Speed: {BMW.speed}, Model: {BMW.model}")

# Use the object's methods (behaviors)
BMW.startCar()      # Output: The BMW X5 is starting.
BMW.changeGear(3)   # Output: The BMW X5 is changing to gear 3.
BMW.slowDown()      # Output: The BMW X5 is slowing down.
BMW.brake()         # Output: The BMW X5 is braking.




#Encapsulation:

# Understanding Access Modifiers in Python:

# Public Attributes:
# By default, all attributes and methods in a class are public unless specified otherwise. Public attributes can be accessed from outside the class directly.
# Private Attributes:
# In your code, the attributes __account_number and __balance are defined with a double underscore prefix (__). 
# Protected Attributes:
# Although you haven't used the protected attribute convention (a single underscore prefix _), you could implement it by prefixing any attribute with a single underscore if you want to indicate that it is intended for internal use and should not be accessed directly from outside the class. However, it's not enforced in Python like it is in some other languages.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

# Create a BankAccount object
account = BankAccount("123456", 1000)

# Accessing balance through getter
print(f"Initial Balance: {account.get_balance()}")  # Output: 1000

# Depositing money
account.deposit(500)  # Output: Deposited: 500. New balance: 1500

# Withdrawing money
account.withdraw(200)  # Output: Withdrew: 200. New balance: 1300

# Attempting to access private attribute directly (will raise an error)
# print(account.__balance)  # Raises AttributeError

# Accessing balance again through getter
print(f"Current Balance: {account.get_balance()}")  # Output: 1300




#Polymorphism:
#poly means --> Many  and morphism --> Forms (Behaves meany forms)
# The example you provided is a perfect real-world scenario to explain polymorphism. In this case, the same person exhibits different behaviors depending on the context. This aligns well with the concept of polymorphism, where an object (the person) can behave differently based on where or how it is used.

#Explaination:
# Base Class (Person):

# We define a base class Person, which includes an abstract method behave(). This is an abstract method because it raises a NotImplementedError, indicating that subclasses must override and implement this method.
# Derived Classes (Student, Customer, Son, Passenger):

# Four subclasses (Student, Customer, Son, Passenger) inherit from Person, and each one implements the behave() method differently to represent how the person behaves in different situations.
# Polymorphism in Action:

# The describe_behavior() function accepts any object that is an instance of the Person class (or its subclasses) and calls the behave() method on it.
# Despite calling the same behave() method, the actual behavior (output) changes depending on which subclass's object is passed. This is the essence of polymorphism—one interface, different behaviors.



class Person:
    def behave(self):
        raise NotImplementedError("Subclass must implement this method")

class Student(Person):
    def behave(self):
        return "In school, the person behaves like a student."

class Customer(Person):
    def behave(self):
        return "In the shopping mall, the person behaves like a customer."

class Son(Person):
    def behave(self):
        return "At home, the person behaves like a son."

class Passenger(Person):
    def behave(self):
        return "In the bus, the person behaves like a passenger."

# Function that accepts any "Person" and calls the behave() method
def describe_behavior(person):
    print(person.behave())

# Create objects representing the person in different contexts
student = Student()
customer = Customer()
son = Son()
passenger = Passenger()

# Demonstrating polymorphism by calling the same method on different objects
describe_behavior(student)    # Output: In school, the person behaves like a student.
describe_behavior(customer)   # Output: In the shopping mall, the person behaves like a customer.
describe_behavior(son)        # Output: At home, the person behaves like a son.
describe_behavior(passenger)  # Output: In the bus, the person behaves like a passenger.










#Abstraction:
# Abstraction in Python is one of the key concepts of Object-Oriented Programming (OOP) that allows you to hide complex implementation details and only expose the necessary parts of the object to the user.

#Explaination:
# Key Points of the Example:
# Abstract Base Class (Animal): Defines an interface (sound) that must be implemented by any subclass.
# Abstract Method (sound): Subclasses must provide their own implementation of this method. If they don’t, you can't instantiate them.
# Concrete Subclasses (Dog, Cat): These classes provide specific implementations of the sound() method.

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Base Class
    @abstractmethod
    def sound(self):
        pass  # Abstract method

class Dog(Animal):  # Concrete class
    def sound(self):
        return "Bark"
    
class Cat(Animal):  # Concrete class
    def sound(self):
        return "Meow"

# You can't instantiate an abstract class directly
# animal = Animal()  # This will raise an error

# But you can instantiate its concrete subclasses
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow



#ATM example
from abc import ABC, abstractmethod

# Abstract base class defining the structure of an ATM
class ATM(ABC):

    @abstractmethod
    def check_balance(self):
        pass
    
    @abstractmethod
    def deposit_cash(self, amount):
        pass
    
    @abstractmethod
    def withdraw_cash(self, amount):
        pass
    
    @abstractmethod
    def mini_statement(self):
        pass

# Concrete class implementing the ATM interface
class BankATM(ATM):
    
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []  # To store transaction history
    
    def check_balance(self):
        return f"Your balance is: ${self.balance}"
    
    def deposit_cash(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ${amount}")
            return f"Deposited: ${amount}\nNew balance: ${self.balance}"
        else:
            return "Deposit amount must be positive."
    
    def withdraw_cash(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount}")
            return f"Please collect your cash: ${amount}\nRemaining balance: ${self.balance}"
        else:
            return "Insufficient balance."
    
    def mini_statement(self):
        if not self.transactions:
            return "No transactions available."
        return "\n".join(self.transactions)

# Usage example
atm = BankATM(1000)  # Setting initial balance as $1000

# User interaction (simulated)
print(atm.check_balance())         # Check balance
print(atm.deposit_cash(300))       # Deposit $300
print(atm.withdraw_cash(200))      # Withdraw $200
print(atm.mini_statement())         # Print mini statement






#Inheritance:
#Def: It acquires the properties of one object class to the another object class
#Reusability
# Summary of Inheritance Types:
# Single Inheritance: One child class inherits from one parent class.
# Multiple Inheritance: One child class inherits from multiple parent classes.
# Multilevel Inheritance: A class inherits from another class, forming a chain.
# Hierarchical Inheritance: Multiple child classes inherit from the same parent class.
# Hybrid Inheritance: A combination of two or more types of inheritance.


# Single Inheritance:
class Parent:
    def parent_method(self):
        return "This is a parent method."

class Child(Parent):
    def child_method(self):
        return "This is a child method."

obj = Child()
print(obj.parent_method())  # Output: This is a parent method.
print(obj.child_method())   # Output: This is a child method.

# Multiple Inheritance:
class Father:
    def father_method(self):
        return "This is a method from Father."

class Mother:
    def mother_method(self):
        return "This is a method from Mother."

class Child(Father, Mother):
    pass

obj = Child()
print(obj.father_method())  # Output: This is a method from Father.
print(obj.mother_method())  # Output: This is a method from Mother.


# Multilevel Inheritance:
class Grandparent:
    def grandparent_method(self):
        return "This is a grandparent method."

class Parent(Grandparent):
    def parent_method(self):
        return "This is a parent method."

class Child(Parent):
    def child_method(self):
        return "This is a child method."

obj = Child()
print(obj.grandparent_method())  # Output: This is a grandparent method.
print(obj.parent_method())       # Output: This is a parent method.
print(obj.child_method())        # Output: This is a child method.


# Hierarchical Inheritance: 
class Parent:
    def parent_method(self):
        return "This is a parent method."

class Child1(Parent):
    def child1_method(self):
        return "This is a method from Child1."

class Child2(Parent):
    def child2_method(self):
        return "This is a method from Child2."

obj1 = Child1()
obj2 = Child2()

print(obj1.parent_method())  # Output: This is a parent method.
print(obj2.parent_method())  # Output: This is a parent method.


# Hybrid Inheritance
class Grandparent:
    def grandparent_method(self):
        return "This is a grandparent method."

class Parent(Grandparent):
    def parent_method(self):
        return "This is a parent method."

class Child1(Parent):
    def child1_method(self):
        return "This is a method from Child1."

class Child2(Parent):
    def child2_method(self):
        return "This is a method from Child2."

obj = Child1()
print(obj.grandparent_method())  # Output: This is a grandparent method.
print(obj.parent_method())       # Output: This is a parent method.
