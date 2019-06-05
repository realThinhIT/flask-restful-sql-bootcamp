import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

# CREATE NEW USER TABLE
create_user_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        username TEXT,
        password TEXT
    )
"""

cursor.execute(create_user_table_query)

# CREATE NEW USERS
users = [
    ('Thinh Nguyen', 'thinhnd', '12345678')
]
insert_users_query = """
    INSERT INTO users (name, username, password)
    VALUES (?, ?, ?)
"""

cursor.executemany(insert_users_query, users)

connection.commit()

connection.close()