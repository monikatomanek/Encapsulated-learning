# This file is part of the Encapsulated-learning repo by Monika Tomanek.
# Demo script using config values from .env
# For educational use only.

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

# Simulate a DB connection string (not actually connecting to anything)
print("Connecting to database...")
print(f"Host: {DB_HOST}")
print(f"Database: {DB_NAME}")
print(f"User: {DB_USER}")

if DB_USER and DB_PASSWORD:
    print("Connection successful (pretend)")
else:
    print("Missing credentials. Please check your .env file.")
