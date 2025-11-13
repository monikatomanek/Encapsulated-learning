# This file is part of the Encapsulated-learning repo by Monika Tomanek.
# Librarian class - uses class and static methods in the library system.
# For educational use only.

class Librarian:
    registered_librarians = []  # class variable

    def __init__(self, name):
        self.name = name
        Librarian.registered_librarians.append(name)

    def assist_user(self, user):
        print(f"{self.name} is assisting {user.name}.")

    @classmethod
    def total_librarians(cls):
        return len(cls.registered_librarians)

    @staticmethod
    def format_item_title(title):
        return title.title()
