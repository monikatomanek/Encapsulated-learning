# This file is part of the Encapsulated-learning repo by Monika Tomanek.
# User class demonstrating encapsulation in a library system.
# For educational use only.

class User:
    def __init__(self, name, max_items=3):
        self.name = name
        self.__max_items = max_items
        self.__borrowed_items = []

    def borrow_item(self, item):
        if item.is_checked_out():
            print(f"{item.title} is already checked out.")
        elif len(self.__borrowed_items) >= self.__max_items:
            print(f"{self.name} has reached the borrowing limit.")
        else:
            item.checkout()
            self.__borrowed_items.append(item)

    def return_item(self, item):
        if item in self.__borrowed_items:
            item.return_item()
            self.__borrowed_items.remove(item)
        else:
            print(f"{self.name} did not borrow {item.title}.")

    def list_borrowed_items(self):
        if not self.__borrowed_items:
            print(f"{self.name} has no borrowed items.")
        else:
            print(f"{self.name}'s borrowed items:")
            for item in self.__borrowed_items:
                print(" -", item.get_description())

    def get_borrow_count(self):
        return len(self.__borrowed_items)
