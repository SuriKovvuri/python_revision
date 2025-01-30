class Car:
    def __init__(self, color, weight, cost, speed):
        """
        Initialize a Car object with color, weight, cost, and speed.
        """
        self.color = color
        self.weight = weight
        self.cost = cost
        self.speed = speed

    def start(self):
        """Display the car's color when it starts."""
        print(f"The car has started. Color: {self.color}")

    def change_gear(self, gear):
        """Change the car's gear."""
        print(f"Gear changed to {gear}. Weight of car: {self.weight}")

    def slow_down(self, gear):
        """Slow down the car using a specific gear."""
        print(f"Car is slowing down using gear {gear}. Current cost: {self.cost}")

    def brake(self):
        """Apply brakes to stop the car."""
        print(f"Car is stopping. Current speed: {self.speed}")


# Create a car object
car_obj = Car("Green", "1 ton", "5 Lakh", "1200cc")

# Call methods on the car object
car_obj.start()
car_obj.change_gear(2)
car_obj.slow_down(1)
car_obj.brake()





class Student:
    def __init__(self, name, age, grade):
        # Initialize the student's details
        self.name = name
        self.age = age
        self.grade = grade
        # Removed unnecessary print in constructor

    def display_name(self):
        """Display the student's name"""
        print(f"Name is {self.name}")

    def display_age(self):
        """Display the student's age"""
        print(f"Age is: {self.age}")
    
    def display_grade(self):
        """Display the student's grade"""
        print(f"Grade is: {self.grade}")
        

# Create a student object
obj = Student('Suri', 25, "A+")

# Call methods to display student's details
obj.display_name()
obj.display_age()
obj.display_grade()
