from src.v1 import CRUD
from typing import TypedDict


class User(TypedDict):
    id: int
    name: str


# an extension of our crud to allow types
# this way we aren't working with raw data
# much cleaner but less generalized
class UserDB:
    def __init__(self):
        self.db = CRUD("users")

    def read(self, id: int) -> User | None:
        name = self.db.read(id)

        if name is not None:
            return User(id=id, name=name)
        return None

    def put(self, user: User) -> User | None:
        old_name = self.db.put(user["id"], self._as_dict(user))

        if old_name is not None:
            return User(id=user["id"], name=old_name)
        return None

    def delete(self, id: int) -> User | None:
        old_name = self.db.delete(id)

        if old_name is not None:
            return User(id=id, name=old_name)
        return None

    def _as_dict(self, user: User) -> dict[str, str | int]:
        return {"id": user["id"], "name": user["name"]}
