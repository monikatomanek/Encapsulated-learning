# Library System - OOP Demonstration

This project is part of the `Encapsulated-learning` repository by [Monika Tomanek](https://github.com/monikatomanek) and is designed to demonstrate Object-Oriented Programming (OOP) principles in Python using a basic library management system.

## Overview

The system models a simplified library with the following entities:

* **LibraryItem** (abstract class): Base for all items in the library
* **Book**: Concrete implementation of a library item
* **User**: Can borrow and return items, with encapsulated borrowing logic
* **Librarian**: Demonstrates class and static methods for utility tasks
* **main.py**: A script that ties everything together and demonstrates functionality

## OOP Concepts Demonstrated

| Concept        | Where It Appears                     |
| -------------- | ------------------------------------ |
| Abstraction    | `LibraryItem` (abstract base class)  |
| Inheritance    | `Book` inherits from `LibraryItem`   |
| Encapsulation  | `User` manages borrowing privately   |
| Polymorphism   | Overridden methods like `checkout()` |
| Class Methods  | `Librarian.total_librarians()`       |
| Static Methods | `Librarian.format_item_title()`      |

## How to Run

1. Clone the repository
2. Navigate to the `library-system/` folder
3. Run the script:

```bash
python main.py
```

You should see output demonstrating book checkout, return behavior, borrow limits, and librarian actions.

## Educational Use

This code is designed for learning and educational use only. It is not intended for production use and omits certain real-world error handling for clarity.

---

If you find this helpful, feel free to star the repo, fork it, or contribute ideas or corrections.

> Authored and maintained by Monika Tomanek
