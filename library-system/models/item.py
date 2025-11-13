# This file is part of the Encapsulated-learning repo by Monika Tomanek.
# Abstract base for all library items.
# For educational use only.

from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self._is_checked_out = False

    @abstractmethod
    def checkout(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    def get_description(self):
        return f"{self.title} by {self.author} ({self.year})"

    def is_checked_out(self):
        return self._is_checked_out
