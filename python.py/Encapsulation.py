# Public Method

class ABC:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):  # Public method
        print(f"{self.name},{self.age}")
        
obj = ABC(name="Suri", age=25)
obj.info()  # Calling the public method


# Protected Method
class ABC:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def _info(self):  # Protected method
        print(f"{self.name},{self.age}")
        
obj = ABC(name="Suri", age=25)
obj._info()  # Calling the protected method


#Private
class ABC:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __info(self):
        print("private Method started")
    def display(self):
        print(f"{self.name},{self.age}")
obj = ABC(age=24,name="Suri")
obj.display()
obj.__info()  #calling private private 