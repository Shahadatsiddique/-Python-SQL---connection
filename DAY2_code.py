import mysql.connector

connection=mysql.connector.connect(
    host="127.0.0.1",
        user="root",
        password="Password",
        database="library"
)
print("Connected to Library database successfully!")

cursor=connection.cursor()

#showing all table
cursor.execute("show tables")
for table in cursor:
    print(table)


#describe one table
cursor.execute("describe books")
for columns in cursor:
    print(columns)


#describing other table
cursor.execute("DESCRIBE issued_books")
for column in cursor:
    print(column)


#describing another book
cursor.execute("DESCRIBE fines")
for column in cursor:
    print(column)


cursor.execute("SELECT * FROM members")
for row in cursor:
    print(row)


cursor.execute("SELECT * FROM issued_books")
for row in cursor:
    print(row)


cursor.execute("""
    SELECT book_id, title, available_copies
    FROM books
""")
for row in cursor:
    print(row)


cursor.execute("SELECT * FROM fines")
for row in cursor:
    print(row)


cursor.execute("SELECT MAX(issue_id) FROM issued_books")
result = cursor.fetchone()
print("Highest issue ID:", result[0])


cursor.execute("""
    SELECT member_id, name
    FROM members
    WHERE member_id = %s
""", (101,))
member = cursor.fetchone()
print("Member:", member)


cursor.execute("""
    SELECT book_id, title, available_copies
    FROM books
    WHERE book_id = %s
""", (3,))
book = cursor.fetchone()
print("Book:", book)



from datetime import date
today = date.today()
# print("Today's date:", today)


insert issue
cursor.execute("""
    INSERT INTO issued_books
    (issue_id, book_id, member_id, issue_date, return_date)
    VALUES (%s, %s, %s, %s, %s)
""", (1006, 3, 101, today, None))
connection.commit()

verify
cursor.execute("""
    SELECT *
    FROM issued_books
    WHERE issue_id = 1006
""")
issue = cursor.fetchone()
print("Issue 1006:", issue)


cursor.execute("""
    SELECT book_id, title, available_copies
    FROM books
    WHERE book_id = %s
""", (3,))
book = cursor.fetchone()
print("Current book:", book)


cursor.execute("""
    UPDATE books
    SET available_copies = available_copies - 1
    WHERE book_id = %s
""", (3,))
connection.commit()
print("Book availability updated.")

cursor.execute("""
    UPDATE books
    SET available_copies = 3
    WHERE book_id = %s
""", (3,))
connection.commit()
print("Book availability corrected.")


cursor.execute("""
    SELECT book_id, title, available_copies
    FROM books
    WHERE book_id = %s
""", (3,))
book = cursor.fetchone()
print("Updated book:", book)


cursor.execute("""
    SELECT issue_id, book_id, member_id, issue_date, return_date
    FROM issued_books
    WHERE issue_id = %s
""", (1006,))
issue = cursor.fetchone()
print("Issue:", issue)


return_date = date.today()
print("Return date:", return_date)


cursor.execute("""
    UPDATE issued_books
    SET return_date = %s
    WHERE issue_id = %s
""", (return_date, 1006))
connection.commit()
print("Return date updated.")


cursor.execute("""
    UPDATE books
    SET available_copies = available_copies + 1
    WHERE book_id = %s
""", (3,))
connection.commit()
print("Book availability increased.")


cursor.execute("""
    SELECT book_id, title, available_copies
    FROM books
    WHERE book_id = %s
""", (3,))
book = cursor.fetchone()
print("Final book:", book)


cursor.execute("""
    UPDATE books
    SET available_copies = available_copies - 1
    WHERE book_id = %s
""", (3,))
print("Temporary change:", cursor.rowcount)
cursor.execute("""
    UPDATE books
    SET available_copies = available_copies + 1
    WHERE book_id = %s
""", (3,))
connection.commit()
print("Transaction committed.")



cursor.execute("""
    SELECT
        issued_books.issue_id,
        books.title,
        members.name,
        issued_books.issue_date,
        issued_books.return_date
    FROM issued_books
    JOIN books
        ON issued_books.book_id = books.book_id
    JOIN members
        ON issued_books.member_id = members.member_id
""")
for row in cursor:
    print(row)


cursor.execute("""
    SELECT
        issued_books.issue_id,
        books.title,
        members.name,
        issued_books.issue_date
    FROM issued_books
    JOIN books
        ON issued_books.book_id = books.book_id
    JOIN members
        ON issued_books.member_id = members.member_id
    WHERE issued_books.return_date IS NULL
""")
for row in cursor:
    print(row)


cursor.execute("""
    SELECT
        books.title,
        members.name,
        members.email,
        issued_books.issue_date
    FROM issued_books
    JOIN books
        ON issued_books.book_id = books.book_id
    JOIN members
        ON issued_books.member_id = members.member_id
    WHERE issued_books.return_date IS NULL
""")

for row in cursor:
    print(row)


'''
FUNCTIONS

We will organize our library operations
into separate functions.
'''




def get_book(book_id):
    cursor.execute("""
        SELECT book_id, title, author, available_copies
        FROM books
        WHERE book_id = %s
    """, (book_id,))
    book = cursor.fetchone()
    return book

book_id = int(input("Enter book ID: "))
book = get_book(book_id)
if book:
    print("Book:", book)
else:
    print("Book not found.")



def get_member(member_id):
    cursor.execute("""
        SELECT member_id, name, email
        FROM members
        WHERE member_id = %s
    """, (member_id,))
    member = cursor.fetchone()
    return member

member_id = int(input("Enter member ID: "))
member = get_member(member_id)
if member:
    print("Member:", member)
else:
    print("Member not found.")



def get_active_issues():
    cursor.execute("""
        SELECT
            issued_books.issue_id,
            books.title,
            members.name,
            issued_books.issue_date
        FROM issued_books
        JOIN books
            ON issued_books.book_id = books.book_id
        JOIN members
            ON issued_books.member_id = members.member_id
        WHERE issued_books.return_date IS NULL
    """)
    issues = cursor.fetchall()
    return issues

issues = get_active_issues()
for issue in issues:
    print(issue)



def close_connection():
    cursor.close()
    connection.close()
    print("Database connection closed.")
close_connection()


book = get_book(3)

print("Current book:", book)
