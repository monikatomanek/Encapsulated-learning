---

This guide is part of the `Encapsulated-learning` repo by [Monika Tomanek](https://github.com/monikatomanek).
Do not redistribute without attribution.
----------------------------------------

# Object-Oriented Programming (OOP) in Python - A Descriptive Guide

This is a detailed and explanatory guide to understanding Object-Oriented Programming (OOP) in Python. It includes structured content, real-world analogies, practical code examples, and common pitfalls. It is intended to help learners deeply understand OOP beyond superficial summaries.

## Table of Contents

1. What is OOP?
2. Class and Object
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction
7. Class and Static Methods

## 1. What is OOP?

OOP (Object-Oriented Programming) is a paradigm where code is organized around "objects" which combine data and behavior. Instead of using functions and variables scattered around, OOP groups related concepts into entities.

### Benefits:

* Cleaner, modular code
* Logical mapping to real-world problems
* Easier scalability and maintenance

## 2. Class and Object

A class defines the blueprint. An object is an instance built from it.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

car1 = Car("Toyota", "Corolla")
car1.drive()
```

### Without OOP:

```python
def drive_car(brand, model):
    print(f"{brand} {model} is driving.")
```

This quickly gets messy with multiple items and behaviors. OOP organizes this better.

## 3. Encapsulation

Encapsulation hides internal data and allows controlled access.

```python
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            self.__speed = 0
        else:
            self.__speed = value
```

This prevents invalid states, like negative speed.

## 4. Inheritance

Inheritance allows child classes to reuse and extend parent class behavior.

```python
class Car:
    def drive(self):
        print("Driving...")

class ElectricCar(Car):
    def charge(self):
        print("Charging...")
```

## 5. Polymorphism

Polymorphism allows different classes to use the same method name but different behavior.

```python
class ManualCar(Car):
    def drive(self):
        print("Manual drive")

class AutoCar(Car):
    def drive(self):
        print("Automatic drive")
```

## 6. Abstraction

Abstraction exposes only the relevant methods and hides inner details.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Car drives")
```

## 7. Class and Static Methods

```python
class Car:
    total_cars = 0

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def show_total_cars(cls):
        print(cls.total_cars)

    @staticmethod
    def convert_speed(kph):
        return kph * 0.621371
```

---

## This guide is part of the `Encapsulated-learning` repo by [Monika Tomanek](https://github.com/monikatomanek). For educational use only.
