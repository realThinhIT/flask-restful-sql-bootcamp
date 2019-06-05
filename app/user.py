import sqlite3


class User:
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        find_by_username_query = """
            SELECT * FROM users
            WHERE 
                username = ?
        """
        result = cursor.execute(find_by_username_query, (username,))
        row = result.fetchone()

        connection.close()

        return cls(*row) if row else None

    @classmethod
    def find_by_id(cls, userId):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        find_by_username_query = """
                SELECT * FROM users
                WHERE 
                    id = ?
            """
        result = cursor.execute(find_by_username_query, (userId,))
        row = result.fetchone()

        connection.close()

        return cls(*row) if row else None