import sqlite3  

def create_books_database(db_file):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        print("SQLite version:", sqlite3.version)

        # Commit the changes (in this case, creating the database)
        conn.commit()

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        # Close the connection, whether an exception occurred or not
        if conn:
            conn.close()

# Specify the name of your SQLite database file
db_file = "database.db"

# Call the function to create the SQLite database
create_books_database(db_file)
