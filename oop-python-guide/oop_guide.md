---

This guide is part of the `Encapsulated-learning` repo by [Monika Tomanek](https://github.com/monikatomanek). Do not redistribute without attribution.

---

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

OOP (Object-Oriented Programming) is a programming paradigm that organizes code around objects. These objects bundle data and behavior together.

### Benefits of OOP:

- Cleaner, modular code
- Logical structure aligned with real-world entities
- Reusable components and extensible design
- Easier to maintain, scale, and debug

Without OOP, a program becomes a large mess of functions and variables with unclear relationships. OOP gives structure.

## 2. Class and Object

A class is a blueprint for creating objects. An object is an instance of a class.

### Code without OOP:

```python
def drive_car(brand, model):
    print(f'{brand} {model} is driving.')

drive_car('Toyota', 'Corolla')
drive_car('Tesla', 'Model 3')
```

This works, but what if you want to manage multiple behaviors like braking, accelerating, parking? You would need to pass `brand` and `model` to every function. This quickly becomes repetitive, error-prone, and hard to organize.

### Code with OOP:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f'{self.brand} {self.model} is driving.')

car1 = Car('Toyota', 'Corolla')
car2 = Car('Tesla', 'Model 3')
car1.drive()
car2.drive()
```

### Common problem without OOP:
- Difficult to manage state (no data attached to behavior)
- Logic and data live in separate places
- Repeated code

OOP allows us to encapsulate state and behavior in one reusable structure.

## 3. Encapsulation

Encapsulation means hiding internal state and exposing controlled access.

### Problem without Encapsulation:

```python
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

car = Car('Ford', 'Focus', -50)  # Speed should not be negative
```

Here, speed can be set to a negative value. There is no check or validation.

### Solution with Encapsulation:

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
            print('Speed cannot be negative. Setting to 0.')
            self.__speed = 0
        else:
            self.__speed = value

car = Car('Ford', 'Focus', -50)
print(car.speed)  # Output: 0
```

The internal variable `__speed` is protected from direct access and validated through a setter.

## 4. Inheritance

Inheritance allows a class to extend the functionality of another.

### Without Inheritance:

```python
class ElectricCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f'{self.brand} {self.model} is driving.')

    def charge(self):
        print(f'{self.brand} {self.model} is charging.')
```

You're repeating `__init__` and `drive` methods.

### With Inheritance:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f'{self.brand} {self.model} is driving.')

class ElectricCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model} is charging.')

my_car = ElectricCar('Tesla', 'Model S')
my_car.drive()
my_car.charge()
```

### Problem avoided:
- Duplicated logic
- Unnecessary repetition
- Lack of structure in related classes

Inheritance groups shared functionality and enables easier scaling.

## 5. Polymorphism

Polymorphism allows different classes to have methods with the same name but different implementations.

### Example:

```python
class Car:
    def drive(self):
        print('Generic driving')

class ManualCar(Car):
    def drive(self):
        print('Manual drive mode')

class AutomaticCar(Car):
    def drive(self):
        print('Automatic drive mode')

cars = [ManualCar(), AutomaticCar()]
for car in cars:
    car.drive()
```

### Problem avoided:
- You don't need to check the type of car
- Code becomes cleaner and interchangeable

## 6. Abstraction

Abstraction allows us to define expected behavior without enforcing implementation.

### Without Abstraction:

There's no common agreement on which methods must be implemented. Anyone can forget `drive()` or `refuel()`.

### With Abstraction:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(Vehicle):
    def drive(self):
        print('Car drives')

    def refuel(self):
        print('Car refuels')
```

Now every subclass of `Vehicle` must implement `drive()` and `refuel()` or Python will raise an error.

### Problem avoided:
- Missing core methods
- Unreliable design contracts

## 7. Class and Static Methods

### Class Method:
Operates on the class itself (shared state).

### Static Method:
Does not use object or class state. Just a utility.

```python
class Car:
    total_cars = 0

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def show_total_cars(cls):
        print(f'Total cars created: {cls.total_cars}')

    @staticmethod
    def convert_speed_to_mph(kph):
        return kph * 0.621371

Car()
Car()
Car.show_total_cars()  # Output: Total cars created: 2
print(Car.convert_speed_to_mph(100))  # Output: 62.1371
```

---

## Summary

This guide offers more than syntax. It explains why OOP matters and how it prevents real-world issues:

- Classes reduce repetition and organize related data
- Encapsulation prevents invalid data states
- Inheritance reduces duplication and enables structure
- Polymorphism enables flexibility and cleaner interfaces
- Abstraction defines contracts for consistency
- Class and static methods organize logic properly

Use this guide as a reference for building clean, structured Python code.

---

This guide is part of the `Encapsulated-learning` repo by [Monika Tomanek](https://github.com/monikatomanek). For educational use only.
