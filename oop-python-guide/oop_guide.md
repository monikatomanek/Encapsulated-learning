---

This guide is part of the `Encapsulated-learning` repo by [Monika Tomanek](https://github.com/monikatomanek).
Do not redistribute without attribution.

---

# Object-Oriented Programming (OOP) in Python — Full Guide with Comparisons and Explanations

This is not just a cheat sheet. It’s a full learning walkthrough.
You’ll learn what OOP is, what problems it solves, how it compares to non-OOP code, and what changes with each core concept: classes, encapsulation, inheritance, polymorphism, abstraction, class methods and static methods.

---

## Table of Contents

1. What is OOP?
2. Class and Object
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction
7. Class and Static Methods

---

## 1. What is OOP?

OOP (Object-Oriented Programming) is a programming style where you group **data** and the **code that operates on that data** together into reusable building blocks called **objects**.

### Why does this matter?
Without OOP, your code becomes scattered. Data lives in one place, logic in another, and you keep passing things around manually.
With OOP, everything related to a concept (like a `Car`) lives inside one neat structure.

### Problems OOP solves:
- Data and logic are scattered and fragile
- Copy-paste reuse everywhere
- State is not tied to logic
- Adding new features creates chaos

---

## 2. Class and Object

### Problem without OOP:
You have to pass the same values (`brand`, `model`, etc.) to every function manually.

```python
def drive_car(brand, model):
    print(f'{brand} {model} is driving.')

drive_car('Toyota', 'Corolla')
drive_car('Tesla', 'Model 3')
```

This works, but what if you want to also add speed, colour, fuel, and methods like brake, reverse, accelerate? You end up with a jungle of repeated arguments.

### Using OOP:

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

### Comparison Table:

| Feature                | Without OOP                              | With OOP                              |
|------------------------|-------------------------------------------|----------------------------------------|
| State handling         | Manual passing of values                  | Data stored inside object              |
| Code organization      | Functions and data scattered              | Bundled in one place                   |
| Adding behavior        | Requires new functions with many params   | Just add a new method to the class     |

---

## 3. Encapsulation

Encapsulation hides and protects internal data from being changed directly in unsafe ways.

### Without Encapsulation:
Anyone can change the value of speed to anything — even invalid values.

```python
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

car = Car('Ford', 'Focus', -50)
```

Now your car has a negative speed. There are no safeguards.

### With Encapsulation:

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

### Comparison Table:

| Feature               | Without Encapsulation      | With Encapsulation                     |
|-----------------------|-----------------------------|------------------------------------------|
| Validation            | None                        | Built-in to setter                       |
| Accidental changes    | Easy to break state         | Protected behind controlled access       |
| Debugging             | Hard to track errors        | Predictable behavior                     |

---

## 4. Inheritance

Inheritance allows you to reuse code across related classes.

### Without Inheritance:
You copy methods across classes and repeat logic.

```python
class ElectricCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f'{self.brand} {self.model} is driving.')
```

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

ecar = ElectricCar('Tesla', 'Model S')
ecar.drive()
ecar.charge()
```

### Comparison Table:

| Feature                | Without Inheritance     | With Inheritance                |
|------------------------|--------------------------|----------------------------------|
| Code duplication       | High                     | Minimal                          |
| New functionality      | Requires copy-pasting    | Add only what’s different        |
| Maintenance            | Repeating updates        | Fix in one place                 |

---

## 5. Polymorphism

Polymorphism lets you define the same method name with different behaviour depending on the class.

### Example:

```python
class Car:
    def drive(self):
        print('Generic car driving')

class ManualCar(Car):
    def drive(self):
        print('Driving with manual gear shifting')

class AutoCar(Car):
    def drive(self):
        print('Driving with automatic transmission')

cars = [ManualCar(), AutoCar()]
for car in cars:
    car.drive()
```

Each object calls the correct `drive()` method without needing `if` statements.

### Problem without Polymorphism:
You’d have to write logic like:

```python
if type(car) == 'Manual':
    manual_drive(car)
elif type(car) == 'Auto':
    auto_drive(car)
```

This is fragile and hard to scale.

---

## 6. Abstraction

Abstraction lets you define *what* something should do without worrying about *how* it does it.

### With abstraction:
Use `ABC` (Abstract Base Class) to define a common interface.

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
        print('Refueling car')
```

If a subclass does not implement all abstract methods, Python raises an error.

---

## 7. Class and Static Methods

### Class Methods:
Operate on the class itself. Useful for tracking shared state.

### Static Methods:
Utility methods that don’t access instance or class state.

```python
class Car:
    total_cars = 0

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def show_total_cars(cls):
        print(f'Total cars created: {cls.total_cars}')

    @staticmethod
    def convert_speed(kph):
        return kph * 0.621371
```

### When to use each:

| Method Type      | Use When                                           |
|------------------|----------------------------------------------------|
| Instance Method  | Access or modify instance-specific data            |
| Class Method     | Work with class-level data or alternate constructors |
| Static Method    | Perform general-purpose tasks with no state access |

---

## Final Thoughts

This guide isn’t just code — it’s a study of how OOP organises your thinking:

- Classes represent things
- Encapsulation keeps things safe
- Inheritance avoids repetition
- Polymorphism lets different things behave in similar ways
- Abstraction sets rules and expectations
- Class and static methods separate shared tools from individual behaviour

You’re not just learning syntax — you’re learning how to **design software**.

---

This guide is part of the `Encapsulated-learning` repo by [Monika Tomanek](https://github.com/monikatomanek). For educational use only.
