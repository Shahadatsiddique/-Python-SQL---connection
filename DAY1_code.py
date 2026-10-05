import mysql.connector

print("MySQL connector imported successfully")

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="YOUR PASSWORD",
    database="library"
)

print("Connected successfully!")

cursor = connection.cursor()


#             showtable
#    -----------------------------
'''
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
'''


#             fetchall()
#    ----------------------------
'''
cursor.execute("""
    SELECT author, title
    FROM books
    WHERE available_copies = 2
""")

rows = cursor.fetchall()
for row in rows:
    print(row)
'''


#            fetchone()
#   -----------------------------
'''
cursor.execute("""
    SELECT author, title
    FROM books
    WHERE available_copies = 2
""")
row = cursor.fetchone()
print(row)
'''

'''////////////////////////////'''


#        fetchone() with book_id
#   -----------------------------
'''
# cursor.execute("""
#     SELECT book_id, title, author, genre
#     FROM books
#     WHERE book_id = 6
# """)
# book = cursor.fetchone()
# print(book)
'''

'''//////////////////////////////'''

#       parameterized fetchone()
#   -----------------------------

def search_book(book_id):
    cursor.execute("""
        SELECT book_id, title, author
        FROM books
        WHERE book_id = %s
    """, (book_id,))

    book = cursor.fetchone()
    return book

book_id = int(input("Enter book ID: "))

book = search_book(book_id)

if book:
    book_id, title, author = book

    print("Book ID:", book_id)
    print("Title:", title)
    print("Author:", author)
else:
    print("Book not found.")




#          python insert
#   ----------------------------
'''
cursor.execute("""
    INSERT INTO books
    (book_id,title, author, genre, total_copies, available_copies)
    VALUES (%s,%s, %s, %s, %s, %s)
""", (
    6,
    "Clean Code",
    "Robert C. Martin",
    "Programming",
    5,
    5
))
connection.commit()
print("Book inserted successfully!")
'''


#          update
#   --------------------
'''
cursor.execute("""
    UPDATE books
    SET available_copies = 4
    WHERE book_id = 6 """)
connection.commit()
print("Book updated successfully!")
'''


#    add one more data
#   ------------------------
'''
cursor.execute("""
    INSERT INTO books
    (book_id, title, author, genre, total_copies, available_copies)
    VALUES (7, 'Test Book', 'Test Author', 'Testing', 1, 1)  """)
connection.commit()
print("Test book inserted!")
'''



#     delete data
#   --------------------
'''
cursor.execute("""
    DELETE FROM books
    WHERE book_id = 7  """)
connection.commit()
print("Test book deleted!")
'''
