class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
    def display_details(self):
        print(f"Title:{self.title}\nAuthor:{self.author}\nPrice:{self.price}")
obj = Book(title="The Alchemist",author="Paulo Coelho",price="299.99")
obj1 = Book(title="Sapiens",author="Yuval Noah Harari",price="499.99")
obj2 = Book(title="Atomic Habits",author="James Clear",price="350.00")
obj.display_details()
obj1.display_details()
obj2.display_details()



#class 
    # Car
# Attributes
    # make: The manufacturer of the car (e.g., Toyota, Tesla).
    # model: The model of the car (e.g., Corolla, Model S).
    # year: The manufacturing year of the car.
    # price: The price of the car.
    # fuel_level: The current fuel level in the car's tank (e.g., percentage or liters).
    # mileage: The car's mileage (kilometers driven or miles per gallon).
# Methods
    # display_details: Prints all the details of the car.
    # start: Simulates starting the car, checking if there's enough fuel.
    # drive: Simulates driving the car, reducing the fuel level and increasing mileage.
    # refuel: Refills the fuel tank.
    # apply_discount: Adjusts the car's price based on a discount percentage.

class Car:
    def __init__(self, make, model, year, price, fuel_level, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.fuel_level = fuel_level
        self.mileage = mileage

    def display_details(self):
        """Displays all details of the car."""
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")
        print(f"Fuel Level: {self.fuel_level}%")
        print(f"Mileage: {self.mileage} km")
        print()

    def start(self):
        """Simulates starting the car."""
        if self.fuel_level > 0:
            print(f"{self.make} {self.model} is starting... 🚗")
        else:
            print(f"{self.make} {self.model} cannot start. Please refuel!")

    def drive(self, distance):
        """Simulates driving the car."""
        fuel_consumption = distance * 0.1  # Assume 10 km per 1% fuel
        if self.fuel_level >= fuel_consumption:
            self.fuel_level -= fuel_consumption
            self.mileage += distance
            print(f"Drove {distance} km. Fuel Level: {self.fuel_level:.1f}%. Mileage: {self.mileage} km.")
        else:
            print(f"Not enough fuel to drive {distance} km. Please refuel.")

    def refuel(self, amount):
        """Refuels the car."""
        if 0 < self.fuel_level + amount <= 100:
            self.fuel_level += amount
            print(f"Refueled {amount}%. Current Fuel Level: {self.fuel_level}%.")
        else:
            print("Cannot refuel beyond the tank's capacity!")

    def apply_discount(self, percentage):
        """Applies a discount to the car's price."""
        if 0 < percentage < 100:
            discount = self.price * (percentage / 100)
            self.price -= discount
            print(f"Discount of {percentage}% applied. New price: {self.price:.2f}")
        else:
            print("Invalid discount percentage.")
# Create car objects
car1 = Car(make="Tesla", model="Model S", year=2022, price=80000, fuel_level=50, mileage=15000)
car2 = Car(make="Toyota", model="Corolla", year=2019, price=20000, fuel_level=80, mileage=45000)

# Display car details
car1.display_details()
car2.display_details()

# Start the cars
car1.start()
car2.start()

# Drive the cars
car1.drive(100)
car2.drive(300)

# Refuel the cars
car1.refuel(30)
car2.refuel(10)

# Apply a discount
car1.apply_discount(10)
car2.apply_discount(15)
