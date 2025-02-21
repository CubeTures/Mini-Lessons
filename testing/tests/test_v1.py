from src.connection import Connection

# tests should be separated by file for the function you're testing
# but here I'll keep them in one file for the sake of the lesson

class DatabaseTests:
    def setup_method(self):
        self.conn = Connection()

class TestCreate(DatabaseTests):
    pass


class TestRead(DatabaseTests):
    pass


class TestDelete(DatabaseTests):
    pass



