import sqlite3
from faker import Faker


def add_fake_user():
    fake = Faker()
    # Connect to the database
    conn = sqlite3.connect('database.db')  # Replace 'your_database.db' with your actual database file
    cursor = conn.cursor()
    for _ in range(5):
        # Generate fake user data
        Firstname = fake.first_name()
        Lastname = fake.last_name()
        Email = fake.email()
        # Insert fake user data into Users table
        cursor.execute("INSERT INTO Users (Firstname, Lastname, Email) VALUES (?, ?, ?)", (Firstname, Lastname, Email))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

add_fake_user()
