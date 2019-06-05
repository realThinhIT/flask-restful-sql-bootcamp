import sqlite3


class Connection:
    __instance = None
    __connection = None

    def __init__(self):
        if self.__instance:
            pass
        else:
            self.__instance = self
            self.get_connection()

    def get_connection(self):
        if self.__connection is None:
            self.__connection = sqlite3.connect('database.db')
        else:
            return self.__connection

    def get_cursor(self):
        return self.get_connection().cursor()