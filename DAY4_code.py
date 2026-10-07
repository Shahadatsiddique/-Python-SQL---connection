import mysql.connector
from datetime import date


connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="YOUR PASSWORD",
    database="library"
)

cursor = connection.cursor()

print("Connected to Library database successfully!")


def get_book(book_id):
    cursor.execute("""
        SELECT book_id, title, author, available_copies
        FROM books
        WHERE book_id = %s
    """, (book_id,))
    book = cursor.fetchone()
    return book


def get_member(member_id):
    cursor.execute("""
        SELECT member_id, name, email
        FROM members
        WHERE member_id = %s
    """, (member_id,))
    member = cursor.fetchone()
    return member


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



def close_connection():
    cursor.close()
    connection.close()
    print("Database connection closed.")



def issue_book(book_id, member_id):
    book = get_book(book_id)
    if not book:
        print("Book not found.")
        return
    print("Book found:", book)


    #member availability check
    member = get_member(member_id)
    if not member:
        print("Member not found.")
        return
    print("Member found:", member)


    #book availability check
    if book[3] <= 0:
        print("Book is not available.")
        return
    print("Book is available.")

    cursor.execute("""
        SELECT issue_id
        FROM issued_books
        WHERE book_id = %s
        AND member_id = %s
        AND return_date IS NULL
    """, (book_id, member_id))
    active_issue = cursor.fetchone()

    if active_issue:
        print("This member already has this book.")
        return


    cursor.execute("SELECT MAX(issue_id) FROM issued_books")
    result = cursor.fetchone()

    next_issue_id = result[0] + 1

    #Insert issue and update book availability
    issue_date = date.today()
    try:
        cursor.execute("""
            INSERT INTO issued_books
            (issue_id, book_id, member_id, issue_date, return_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (next_issue_id, book_id, member_id, issue_date, None))

        cursor.execute("""
            UPDATE books
            SET available_copies = available_copies - 1
            WHERE book_id = %s
        """, (book_id,))

        print("Book issue created and updated successfully.")
        connection.commit()

    except mysql.connector.Error as error:
        connection.rollback()
        print("Error while issuing book:", error)


def return_book(issue_id):
    try:
        cursor.execute("""
            SELECT book_id, member_id, return_date
            FROM issued_books
            WHERE issue_id = %s
        """, (issue_id,))
        issue = cursor.fetchone()

        if not issue:
            print("Issue record not found.")
            return
        print("Issue found:", issue)

        if issue[2] is not None:
            print("Book has already been returned.")
            return

        return_date = date.today()

        cursor.execute("""
            UPDATE issued_books
            SET return_date = %s
            WHERE issue_id = %s
        """, (return_date, issue_id))
        print("Book return date updated.")


        cursor.execute("""
            UPDATE books
            SET available_copies = available_copies + 1
            WHERE book_id = %s
        """, (issue[0],))
        connection.commit()
        print("Book returned successfully.")

    except mysql.connector.Error as error:
        connection.rollback()
        print("Error while returning book:", error)




while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Search Book")
    print("2. Search Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View Active Issues")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Enter book ID: "))
        book = get_book(book_id)
        if book:
            print("Book ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Available Copies:", book[3])
        else:
            print("Book not found.")


    elif choice == "2":
        member_id = int(input("Enter member ID: "))
        member = get_member(member_id)
        if member:
            print("Member ID:", member[0])
            print("Name:", member[1])
            print("Email:", member[2])
        else:
            print("Member not found.")


    elif choice == "3":
        book_id = int(input("Enter book ID: "))
        member_id = int(input("Enter member ID: "))

        issue_book(book_id, member_id)

    elif choice == "4":
        issue_id = int(input("Enter issue ID: "))

        return_book(issue_id)

    elif choice == "5":
        issues = get_active_issues()
        if issues:
            for issue in issues:
                print(issue)
        else:
            print("No active issues found.")

    
    elif choice == "6":
        close_connection()
        break
