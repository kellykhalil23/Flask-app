import sqlite3
from faker import Faker


def add_fake_books():
    fake = Faker()
    # Connect to the database
    conn = sqlite3.connect('database.db')  # Replace 'database.db' with your actual database file
    cursor = conn.cursor()
    for _ in range(5):
        # Generate fake book data
        title = fake.catch_phrase()
        author = fake.name()
        publication_year = fake.random_int(min=1900, max=2022)
        # Insert fake book data into books table
        cursor.execute("INSERT INTO books (Title, author, publicationyear) VALUES (?, ?, ?)", (title, author, publication_year))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

add_fake_books()

