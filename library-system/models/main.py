# This file is part of the Encapsulated-learning repo by Monika Tomanek.
# Demonstration of the complete library system in action.
# For educational use only.

from models.book import Book
from models.user import User
from models.librarian import Librarian

# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction")
book2 = Book("Clean Code", "Robert C. Martin", 2008, "Programming")
book3 = Book("1984", "George Orwell", 1949, "Dystopian")

# Create user
user = User("Alice", max_items=2)

# Create librarian
librarian = Librarian("Margaret")

# Use librarian methods
print("Formatted title:", Librarian.format_item_title("to kill a mockingbird"))
print("Total librarians:", Librarian.total_librarians())

# Simulate borrowing books
user.borrow_item(book1)
user.borrow_item(book2)
user.borrow_item(book3)  # Should fail (limit reached)

# List borrowed books
user.list_borrowed_items()

# Return a book
user.return_item(book1)
user.list_borrowed_items()

# Librarian assists user
librarian.assist_user(user)
