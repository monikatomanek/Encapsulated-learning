# This file is part of the Encapsulated-learning repo by Monika Tomanek.
# Book class - a concrete implementation of LibraryItem.
# For educational use only.

from models.item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def checkout(self):
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self._is_checked_out = True
            print(f"'{self.title}' has been checked out.")

    def return_item(self):
        if not self._is_checked_out:
            print(f"'{self.title}' wasn't checked out.")
        else:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")

    def get_description(self):
        base_desc = super().get_description()
        return f"{base_desc} - Genre: {self.genre}"
