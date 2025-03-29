#Functions: In Python, a function is a block of reusable code that is designed to perform a specific task.
def namefun(name):
    print(f"Hello {name}, How are you")
namefun("Suri")

#Function with arguments and return value
def addition(a,b):
    return a+b
print(addition(10,20))


#Keyword Arguments
def key_word(name,age):
    print(f"name is :{name} and age is: {age}")
key_word(name="suri", age=24)

#Lambda Functions (Anonymous Functions)
#A lambda function is a small anonymous function defined using the lambda keyword. It can have any number of arguments but only one expression.

#Syntax:
#lambda arguments: expression

add = lambda x,y : x+y
print(add(4,5))
