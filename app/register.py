from flask_restful import Resource
from flask import request
from connection import Connection


class UserRegister(Resource):
    def __init__(self):
        self.connection = Connection()
        self.cursor = self.connection.get_connection().cursor()

        pass

    def post(self):
        body = request.get_json()
        query = """
            INSERT INTO users (name, username, password)
            VALUES (?, ?, ?)
        """
        result = self.cursor.execute(query, (body['name'], body['username'], body['password']))
        self.connection.get_connection().commit()

        return {'message': 'User registered successfully!'}, 200
