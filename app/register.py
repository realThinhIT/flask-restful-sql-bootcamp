from flask_restful import Resource
from flask import request
from connection import Connection
import sqlite3


class UserRegister(Resource):
    def __init__(self):
        self.connection = Connection()
        self.cursor = self.connection.get_connection().cursor()
        self.cursor.row_factory = sqlite3.Row

        pass

    def get(self):
        query = """
            SELECT * FROM users
        """
        result = self.cursor.execute(query)
        rows = result.fetchall()

        # Build dictionary
        users = []
        for row in rows:
            users.append({
                'id': row['id'],
                'name': row['name'],
                'username': row['username']
            })

        return {'users': users}, 200

    def post(self):
        body = request.get_json()
        query = """
            INSERT INTO users (name, username, password)
            VALUES (?, ?, ?)
        """
        result = self.cursor.execute(query, (body['name'], body['username'], body['password']))
        self.connection.get_connection().commit()

        return {'message': 'User registered successfully!'}, 200
