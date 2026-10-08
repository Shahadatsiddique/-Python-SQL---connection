
---

# 2. README — Complete Project

For the **main repository README**, I recommend using this as the final version.

```markdown
# Library Management System

A menu-driven Library Management System built using Python and MySQL.

The project was developed step by step to understand how a Python application communicates with a relational database and performs real-world database operations such as searching books, managing members, issuing books, returning books, and viewing active issues.

---

## Project Overview

This project simulates basic library operations using a Python application connected to a MySQL database.

The application allows users to:

- Search for books
- Search for members
- Issue books
- Return books
- View active book issues
- Handle invalid inputs
- Prevent duplicate active issues
- Manage database transactions

The project was built as a practical learning project to strengthen Python, SQL, MySQL, database relationships, and application logic.

---

## Features

### 1. Search Book

Search for a book using its Book ID.

The application displays:

- Book ID
- Title
- Author
- Available copies

---

### 2. Search Member

Search for a library member using their Member ID.

The application displays:

- Member ID
- Name
- Email

---

### 3. Issue Book

A member can issue an available book.

Before creating an issue, the application checks:

- Whether the book exists
- Whether the member exists
- Whether the book is available
- Whether the member already has the same book

When the issue is successful:

- A new issue record is inserted
- Available copies are decreased
- The transaction is committed

---

### 4. Return Book

A member can return an issued book using the Issue ID.

The application checks:

- Whether the issue record exists
- Whether the book has already been returned

When the return is successful:

- Return date is updated
- Available copies are increased
- The transaction is committed

---

### 5. View Active Issues

Displays books that are currently issued and have not yet been returned.

The application uses SQL `JOIN` operations to display information from:

- `issued_books`
- `books`
- `members`

---

### 6. Input Validation

The application handles invalid user input using Python exception handling.

Examples:

```text
Please enter a valid book ID.
Please enter a valid member ID.
Please enter a valid issue ID.
Invalid choice. Please enter a number between 1 and 6.
