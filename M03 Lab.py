# Jordan Bullard
# Inheriting Classes
# This app will take the inputted car values, store, and print them.

class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof):
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        print ("Vehicle type: ", vehicleType) 
        print ("Year: ", year) 
        print ("Make: ", make)
        print ("Model: ", model) 
        print ("Number of doors: ", doors)
        print ("Type of roof: ", roof)

car = input("Enter your car type: ")
Vehicle(car)
year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("2 or 4 doors: ")
roof = input("Solid or sun roof: ")
Automobile(car, year, make, model, doors, roof)
