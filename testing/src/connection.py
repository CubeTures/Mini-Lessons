import sqlite3
from typing import Any


class Connection:
    """
    A simple wrapper around the base sqlite3 library to execute commands on a local database.
    """

    conn: sqlite3.Connection
    cur: sqlite3.Cursor

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()

    def execute(self, command: str, params: tuple[Any, ...] | None = None):
        if params:
            self.cur.execute(command, params)
        else:
            self.cur.execute(command)
        self.conn.commit()

    def fetch(self):
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()
