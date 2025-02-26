from src.connection import Connection


class DatabaseTests:
    def setup_method(self):
        self.conn = Connection()
        self.conn.execute("DROP TABLE IF EXISTS tests")
        self.conn.execute("CREATE TABLE tests (id INTEGER PRIMARY KEY, name TEXT)")
        self.conn.execute('INSERT INTO tests VALUES (0, "Name A")')

    def teardown_method(self):
        del self.conn


class TestRead(DatabaseTests):
    def test_read_item(self):
        self.conn.execute("SELECT name FROM tests WHERE id = 0")
        assert self.conn.fetch()[0][0] == "Name A"


class TestPut(DatabaseTests):
    def test_put_item(self):
        self.conn.execute('INSERT INTO tests VALUES (1, "Name B")')
        self.conn.execute("SELECT name FROM tests WHERE id = 1")
        assert self.conn.fetch()[0][0] == "Name B"


class TestDelete(DatabaseTests):
    def test_delete_item(self):
        self.conn.execute('INSERT INTO tests VALUES (2, "Name C")')
        self.conn.execute("SELECT name FROM tests WHERE id = 2")
        self.conn.execute("DELETE FROM tests WHERE id = 2")
        self.conn.execute("SELECT COUNT(*) FROM tests")
        assert self.conn.fetch()[0][0] == 1
