from src.v2 import UserDB
from v2_models import user_0, user_1


# 0. extensive testing suite excluded for brevity
# 1. why is this testing suite unoptimal? Hint: it has to do with the code of v2 itself, not the tests
# 2. the different types of testing: unit, integration, and end-to-end
class TestUserDB:
    def setup_method(self):
        self.db = UserDB()
        self.db.put(user_0)

    def test_get_valid_user(self):
        user = self.db.read(user_0["id"])
        assert user == user_0

    def test_put_user(self):
        old_user = self.db.put(user_1)
        assert old_user == None

        user = self.db.read(user_1["id"])
        assert user == user_1

    def test_delete_user(self):
        old_user = self.db.delete(user_0["id"])
        assert old_user == user_0
