# Library Management System — Day 5

## Overview

Day 5 focused on testing, error handling, edge-case handling, and code cleanup for the Python + MySQL Library Management System.

The main goal was to make the application more reliable by testing different user inputs and database operations and by removing unnecessary testing/debug output from the final application flow.

---

## Day 5 Objectives

- Test invalid menu choices
- Handle invalid ID inputs
- Test non-existing books, members, and issue records
- Prevent duplicate active book issues
- Test successful book issue and return operations
- Verify transaction handling using `commit()` and `rollback()`
- Test already-returned books
- Test the complete issue → return → reissue flow
- Clean unnecessary testing/debug output
- Perform final application testing

---

## Error Handling

The application handles invalid user input using `try-except`.

Example:

```python
try:
    book_id = int(input("Enter book ID: "))
except ValueError:
    print("Please enter a valid book ID.")
