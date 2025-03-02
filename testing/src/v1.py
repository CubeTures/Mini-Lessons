from src.connection import Connection


class CRUD:
    def __init__(self, table: str):
        self.table = table
        self.conn = Connection()
        self.conn.execute(f"DROP TABLE IF EXISTS {table}")
        self.conn.execute(f"CREATE TABLE {table} (id INTEGER PRIMARY KEY, name TEXT)")

    # return the item's name with the id (if any)
    def read(self, id: str | int) -> str | None:
        self.conn.execute(f"SELECT name FROM {self.table} WHERE id = {id}")
        result = self.conn.fetch()

        if len(result) == 0:
            return None
        return result[0][0]

    # return the overwritten object (if any)
    def put(self, id: str | int, item: dict[str, str | int]) -> str | None:
        old = self.read(id)
        self.conn.execute(
            f"INSERT INTO {self.table} values {self._serialize_item(item)}"
        )
        return old

    # return the deleted item (if any)
    def delete(self, id: str | int) -> str | None:
        old = self.read(id)
        self.conn.execute(f"DELETE FROM {self.table} where id = {id}")
        return old

    def _serialize_item(self, item: dict[str, str | int]) -> str:
        try:
            id = item["id"]
            name = item["name"]
            return f"({id}, '{name}')"
        except:
            raise TypeError("Item does not fit expected structure")
