# Using .env Files in Python Projects - A Secure Setup Guide

This guide is part of the `Encapsulated-learning` repository by [Monika Tomanek](https://github.com/monikatomanek) and provides a step-by-step explanation of how to securely handle sensitive credentials (such as API keys and database login info) using a `.env` file in Python projects.

---

## Why do we need this?

When writing code that interacts with external services (APIs, databases, servers), we often need to store sensitive data like:

* API keys
* Database usernames and passwords
* Server URLs

**Never** hardcode these values in your source code — especially in public GitHub repos. This is a major security risk.

Instead, use a `.env` file to store them privately, and make sure Git ignores that file.

---

## Step-by-Step Guide

### Step 1: Install `python-dotenv`

This module allows Python to read key-value pairs from a `.env` file.

Run this in your terminal:

```bash
pip install python-dotenv
```

### Step 2: Create the `.env` file

In the root of your project:

1. Right-click > New File > name it `.env`
2. Add key-value pairs like this:

```
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_NAME=your_database_name
```

> Note: No quotes. No spaces around `=`.

### Step 3: Access those values in your code

Create or update a `config.py` file like so:

```python
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_NAME")
```

This allows you to securely import credentials without exposing them in your code.

### Step 4: Protect your `.env` file from Git

Add the following to your `.gitignore` file:

```
.env
```

This ensures the `.env` file will not be committed or pushed to GitHub.

### Step 5: Tell users to create their own `.env`

In your `README.md`, include a note like this:

> Before running the app, create a `.env` file in the root folder with the following:
>
> ```
> DB_USER=your_username
> DB_PASSWORD=your_password
> DB_HOST=localhost
> DB_NAME=your_database_name
> ```

---

## Summary of the Flow

| Step            | What it Does                | Why it Matters                     |
| --------------- | --------------------------- | ---------------------------------- |
| `.env`          | Stores sensitive values     | Keeps secrets out of code          |
| `.gitignore`    | Prevents `.env` upload      | Keeps secrets off GitHub           |
| `load_dotenv()` | Loads values into memory    | Makes them accessible in Python    |
| `os.getenv()`   | Retrieves individual values | Prevents hardcoding sensitive data |

---

By following this approach, you make your projects safer and more professional — especially if you plan to share them or deploy them in real-world environments.

> Authored and maintained by Monika Tomanek
