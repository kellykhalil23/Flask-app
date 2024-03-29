import sqlite3


def create_books_table(db_file):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create the books table
        cursor.execute('''
            CREATE TABLE Books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                publication_year INTEGER NOT NULL
            );
        ''')

        # Commit the changes (creating the table)
        conn.commit()
        print("Table 'books' created successfully.")

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        # Close the connection, whether an exception occurred or not
        if conn:
            conn.close()

# Specify the name of your SQLite database file
db_file = "database.db"

# Call the function to create the 'books' table
create_books_table(db_file)
