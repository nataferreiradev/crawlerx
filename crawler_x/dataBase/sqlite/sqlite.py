from interface.db import DatabaseInterface
import sqlite3

class SQLiteDatabase(DatabaseInterface):
    _instance = None

    def __new__(cls, db_path="crawler_x.db"):
        if cls._instance is None:
            cls._instance = super(SQLiteDatabase, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect(db_path)
            cls._instance.cursor = cls._instance.conn.cursor()
        return cls._instance

    def execute(self, query: str, params: tuple = ()):
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor.fetchall()

    def insert(self, table: str, data: dict):
        keys = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        values = tuple(data.values())
        query = f"INSERT INTO {table} ({keys}) VALUES ({placeholders})"
        self.execute(query, values)

    def update(self, table: str, data: dict, condition: str, params: tuple = ()):
        set_clause = ', '.join([f"{key}=?" for key in data])
        values = tuple(data.values()) + params
        query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        self.execute(query, values)

    def delete(self, table: str, condition: str, params: tuple = ()):
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute(query, params)

    def close(self):
        self.conn.close()