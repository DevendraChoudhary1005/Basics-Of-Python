class Vehicle:
    def general_usage(self):
        print("General Use: Transportation")

class Car(Vehicle):
    def __init__(self):
        print("Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("Specific Use: Commute to Work, Vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("Motor Cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("Specific Use: Road Trip, Racing")

c = Car()
# c.specific_usage()

b = MotorCycle()
# b.specific_usage()

print(isinstance(c, Car))  #it checks if the 1st variable is an object of the second variable class or not
print(issubclass(Car, Vehicle))

