# This example is part of the Encapsulated-learning repo by Monika Tomanek.
# For educational use only. Do not redistribute without permission.

from abc import ABC, abstractmethod

# Abstraction - base class defining required methods
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

# Parent class
class Car(Vehicle):
    total_cars = 0  # class variable

    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed
        Car.total_cars += 1

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            print("Speed can't be negative. Setting to 0.")
            self.__speed = 0
        else:
            self.__speed = value

    def drive(self):
        if self.speed > 0:
            print(f"{self.brand} {self.model} is driving at {self.speed} km/h.")
        else:
            print(f"{self.brand} {self.model} is parked.")

    def refuel(self):
        print(f"{self.brand} {self.model} is refueling.")

    @classmethod
    def show_total_cars(cls):
        print(f"Total cars created: {cls.total_cars}")

    @staticmethod
    def convert_speed_to_mph(kph):
        return round(kph * 0.621371, 2)

# Inheritance + Polymorphism
class ManualCar(Car):
    def drive(self):
        print(f"{self.brand} {self.model} requires manual gear shifting.")

class AutomaticCar(Car):
    def drive(self):
        print(f"{self.brand} {self.model} changes gears automatically.")

# Example usage
if __name__ == "__main__":
    car1 = ManualCar("Mazda", "MX-5", 60)
    car2 = AutomaticCar("Toyota", "Camry", 80)
    car3 = Car("Ford", "Focus", -50)  # triggers encapsulation check

    for car in [car1, car2, car3]:
        car.drive()
        car.refuel()

    Car.show_total_cars()
    print("Speed in mph:", Car.convert_speed_to_mph(car2.speed))
