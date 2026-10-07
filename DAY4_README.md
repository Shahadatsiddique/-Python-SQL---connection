# Day 4 — Menu-Driven Library Management System

## Overview

Day 4 focused on connecting the Python functions built during the previous days into a simple menu-driven Library Management System.

The goal was to make the application interactive so that users can perform different library operations through a console menu.

## Application Menu

```text
===== LIBRARY MANAGEMENT SYSTEM =====

1. Search Book
2. Search Member
3. Issue Book
4. Return Book
5. View Active Issues
6. Exit
```

## Features Implemented

### 1. Search Book

Users can enter a book ID and view:

* Book ID
* Book title
* Author
* Available copies

The application also handles cases where the requested book does not exist.

### 2. Search Member

Users can search for a member using the member ID.

The application displays:

* Member ID
* Member name
* Email

If the member does not exist, an appropriate message is displayed.

### 3. Issue Book

The existing `issue_book()` function was connected to the menu.

Users provide:

* Book ID
* Member ID

The application then performs the validation and issue process developed during Day 3.

It checks:

* Whether the book exists
* Whether the member exists
* Whether copies are available
* Whether the member already has the same book

If the operation is successful, the issue record is created and the available book copies are updated.

### 4. Return Book

Users can return a book using the issue ID.

The existing `return_book()` function handles:

* Finding the issue record
* Checking whether the book has already been returned
* Updating the return date
* Increasing available book copies

### 5. View Active Issues

The application displays currently active book issues using the existing `get_active_issues()` function.

Only records where the book has not yet been returned are displayed.

### 6. Exit

The Exit option closes the MySQL cursor and database connection before terminating the application.

## Python Concepts Practiced

* `while True` loops
* `if / elif / else`
* User input with `input()`
* Function calls
* Conditional logic
* Iterating through query results with `for` loops
* Database connection management

## Database Concepts Used

The application continues to use the MySQL concepts learned during previous days:

* `SELECT`
* `INSERT`
* `UPDATE`
* `JOIN`
* `WHERE`
* `IS NULL`
* Transactions
* `commit()`
* `rollback()`

## Application Flow

```text
User
  ↓
Menu
  ↓
Select Operation
  ↓
Python Function
  ↓
MySQL Database
  ↓
Process / Validation
  ↓
Result
  ↓
Back to Menu
```

## Testing

The menu was tested for:

* Searching existing books
* Searching existing members
* Issuing books
* Preventing duplicate active issues
* Returning books
* Viewing active issues
* Exiting and closing the database connection

## What I Learned

The main learning from Day 4 was how individual Python functions can be connected together to create a complete console-based application.

Instead of running database functions separately, the menu provides a single interface through which different operations can be performed.

This also helped me understand the basic structure of a real application:

**User Input → Application Logic → Database Operation → Result**

## Day 4 Status

**Completed ✅**

Next: **Day 5 — Testing, Error Handling, and Code Cleanup**
