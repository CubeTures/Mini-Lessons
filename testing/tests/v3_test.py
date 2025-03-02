from pytest import MonkeyPatch
from src.v2 import UserDB, User
from src.v3 import MockCRUD
from v2_models import user_0, user_1


# 1. v3 is a new mock version of our v1, serving as a synthetic, dependency-free storage
# 2. to test the class without changing any of the code from the actual class, we can use dependency injection
# 3. monkey patch
class TestUserDB:
    def setup_method(self):
        def make_db(table: str):
            return MockCRUD(table, {0: self._as_dict(user_0)})

        self.mp = MonkeyPatch()
        self.mp.setattr("src.v2.CRUD", make_db)

        self.db = UserDB()

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

    def _as_dict(self, user: User) -> dict[str, str | int]:
        return {"id": user["id"], "name": user["name"]}
