# Python + MySQL | Library Management System

## 📚 Learning Project

This repository documents my hands-on learning journey of connecting Python with MySQL using a Library Management System as the practical project.

The goal is not just to write SQL queries, but to understand how Python applications communicate with a database and how database operations can be organized into reusable Python code.

---

## ✅ Day 1 — Python + MySQL

### What I Learned

- Installed and imported `mysql.connector`
- Connected Python with a local MySQL database
- Created and used a MySQL cursor
- Used `SHOW TABLES`
- Executed `SELECT` queries from Python
- Used `fetchall()` to retrieve multiple records
- Used `fetchone()` to retrieve a single record
- Used parameterized SQL queries with `%s`
- Performed `INSERT` operations from Python
- Performed `UPDATE` operations from Python
- Performed `DELETE` operations from Python
- Used `connection.commit()` to save database changes
- Checked whether a record exists using `if`
- Created a Python function for database searching
- Passed arguments to a function
- Returned database results using `return`

---

## 🔎 Example: Book Search Function

```python
def search_book(book_id):
    cursor.execute("""
        SELECT book_id, title, author
        FROM books
        WHERE book_id = %s
    """, (book_id,))

    book = cursor.fetchone()
    return book


🚀 Day 2 — Next Step

The next step is to move from individual database examples toward a small working Library Management System.

Day 2 Plan
Build a simple CLI menu
Create functions for different operations
Search books
Add books
Update books
Delete books
View books
Take and validate user input
Work with the existing library database
Start connecting operations with multiple tables
Improve code structure gradually

The focus will be on understanding each step rather than copying a complete application.
