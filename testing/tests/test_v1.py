from src.v1 import CRUD
from models import user_0, user_1, user_2

# tests should be separated by file for the function you're testing but here I'll keep them in one file for the sake of the lesson


class DatabaseTests:
    def setup_method(self):
        self.db = CRUD()


class TestRead(DatabaseTests):
    def test_read_valid_item(self):
        user = self.db.read(user_0["id"])
        assert user == user_0, "Should return existing user with given id"

    def test_read_invalid_item(self):
        user = self.db.read(user_1["id"])
        assert user == None, "Should return None for user not in database"


class TestPut(DatabaseTests):
    def test_put_item(self):
        user = self.db.put(user_1)
        assert user is None


# convoluted, requires 
class TestDelete(DatabaseTests):
    def setup_method(self):
        # prepare delete by adding the user to be deleted
        super().setup_method()
        self.db.put(user_2)

    def teardown_method(self):
        # make sure user is removed if test case fails
        self.db.delete(user_2["id"])

    def test_delete_item(self):
        user = self.db.delete(user_2["id"])
        assert user == user_2, "Should return the deleted user"
