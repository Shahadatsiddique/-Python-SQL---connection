# Library Management System — Day 3

A beginner-friendly **Python + MySQL Library Management System** built step by step as part of my Python + SQL learning journey.

Day 3 focused on converting the database operations from Day 2 into reusable application functions with validation, transaction handling, and proper issue/return workflows.

## Day 3 Focus

* Building reusable application functions
* Book and member validation
* Issue book functionality
* Return book functionality
* Preventing duplicate active issues
* Updating book availability
* Transaction handling with `commit()` and `rollback()`
* Handling database errors
* Testing real database scenarios

## Features Implemented

### Book Operations

* Search and retrieve book information
* Check whether a book exists
* Check available copies

### Member Operations

* Search and retrieve member information
* Check whether a member exists

### Issue Book

The `issue_book()` function:

* Checks whether the book exists
* Checks whether the member exists
* Checks book availability
* Prevents the same member from having the same book issued twice
* Creates a new issue record
* Decreases available book copies
* Uses database transactions

### Return Book

The `return_book()` function:

* Finds the issue record
* Checks whether the issue exists
* Prevents returning an already returned book
* Updates the return date
* Increases available book copies
* Uses database transactions

### Transaction Handling

Database operations that modify multiple tables use:

```python
connection.commit()
```

If a MySQL error occurs:

```python
connection.rollback()
```

This helps keep related database changes consistent.

## Database Tables

The project currently works with these main tables:

* `books`
* `members`
* `issued_books`
* `fines`

The application mainly uses relationships between `books`, `members`, and `issued_books`.

## Tech Stack

* Python 3
* MySQL
* MySQL Connector/Python
* MySQL Workbench
* VS Code

## Concepts Practiced

* Python functions
* Function parameters and return values
* Tuples returned from MySQL queries
* `fetchone()`
* `fetchall()`
* SQL `SELECT`
* SQL `INSERT`
* SQL `UPDATE`
* SQL `JOIN`
* Parameterized queries
* Transactions
* `commit()`
* `rollback()`
* Exception handling
* Database relationships
* Basic application validation

## Testing

The Day 3 functionality was tested using real records in the MySQL database.

Test cases included:

* Valid book and member
* Book not found
* Member not found
* Book unavailable
* Duplicate active issue
* Successful book return
* Already returned book
* Invalid issue ID
* Database update verification

## Project Status

### Day 3 — Completed ✅

Core library operations are now working through Python functions connected to MySQL.

### Next — Day 4

The next step is to connect these functions through a user-friendly menu:

```text
===== LIBRARY MANAGEMENT SYSTEM =====

1. Search Book
2. Search Member
3. Issue Book
4. Return Book
5. View Active Issues
6. Exit
```

The goal is to turn the individual functions into a complete command-line application.

## Security Note

Database credentials should not be stored directly in source code when publishing the project. Before uploading to GitHub, use environment variables or another secure configuration method for database credentials.
