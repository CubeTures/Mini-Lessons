import pytest
from src.v1 import CRUD
from tests.v1_models import user_0, user_1, user_invalid


# 1. tests can now be ran from the UI and results look pretty
# 2. setup_method automatically called at each test run
# 3. cool features of testing: skipping, assert messages, string explanations, expect errors
# 4. how to write a good test suite: regular case coverage, edge, corner, and error cases
class TestCRUD:
    # setup called on every test
    def setup_method(self):
        self.db = CRUD("tests")
        self.db.put(user_0["id"], user_0)

    ##### READ

    # write strings explaining the expected output
    def test_read_valid_item(self):
        user = self.db.read(user_0["id"])
        assert user is not None
        assert user == user_0["name"], "Should return existing user with given id"

    # invalid tests are marked
    def test_read_non_existent_item(self):
        user = self.db.read(user_1["id"])
        assert user == user_1["name"], "Should return None for user not in database"

    ###### PUT

    def test_put_item(self):
        user = self.db.put(user_1["id"], user_1)
        assert user is None

        user = self.db.read(user_1["id"])
        assert user == user_1["name"]

    # skip temporarily without commenting
    @pytest.mark.skip(reason="TODO")
    def test_put_item_overwrite(self):
        pass

    # catch exceptions
    def test_put_invalid_structure(self):
        with pytest.raises(TypeError):
            self.db.put(0, user_invalid)

    ##### DELETE

    def test_delete_item(self):
        user = self.db.delete(user_0["id"])
        assert user == user_0["name"], "Should return the deleted user"

    def test_delete_invalid_item(self):
        user = self.db.delete(user_1["id"])
        assert user == None, "Should return None when deleting a non-existent item"
