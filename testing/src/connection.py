import sqlite3
from typing import Any


class Connection:
    conn: sqlite3.Connection
    cur: sqlite3.Cursor

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()

    def execute(self, command: str) -> list[Any]:
        self.cur.execute(command)
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()
