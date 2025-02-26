import sqlite3


class Connection:
    conn: sqlite3.Connection
    cur: sqlite3.Cursor

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()

    def execute(self, command: str):
        self.cur.execute(command)

    def fetch(self):
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()
