from typing import cast


# a simulated version of v1
# removes dependency on actual database
class MockCRUD:
    # id > dict[str, str | int]
    db: dict[str | int, dict[str, str | int]] = {}

    def __init__(self, table: str, initial_data: dict[str | int, dict[str, str | int]]):
        self.table = table
        self.db = initial_data

    # return the item's name with the id (if any)
    def read(self, id: str | int) -> str | None:
        if id in self.db:
            item = self.db[id]
            return cast(str, item["name"])

        return None

    # return the overwritten object (if any)
    def put(self, id: str | int, item: dict[str, str | int]) -> str | None:
        old = self.read(id)
        self.db[id] = item
        return old

    # return the deleted item (if any)
    def delete(self, id: str | int) -> str | None:
        old = self.read(id)
        del self.db[id]
        return old
