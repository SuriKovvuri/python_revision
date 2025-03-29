#Self

# Error case:
class Myclass():
    x = 5
    def display(self):
        print("X value is ", x)
obj = Myclass()
obj.display()


class Myclass():
    x = 5
    def display(self):
        print("X value is ", self.x)
obj = Myclass()
obj.display()




# __init__ method
class Newclass():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print("Name is:",self.name, "Age is:", self.age)
        
obj = Newclass("Suri", 25)
obj1 = Newclass("Kovvuri",24)
obj.display()
obj1.display()


#difference between __init__ and self


class Myss():
    x = 5
    def __init__(self):
        print("Wlcome to init method")
        
    def display(self):
        print("X value is",self.x)
obj = Myss()
obj1 = Myss()
obj.display()
obj1.display()