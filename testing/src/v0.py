from src.connection import Connection


# 0. a lot of information about setup of testing will be skipped in the lesson in the interest of time, read the notes.md for more info
# 1. this is a simple crud app from getting data from a local sqlite database
# 2. can you find the error? -- not even the type checker will save you
# 3. visual inspection is never enough when writing code
class CRUD:
    def __init__(self, table: str):
        self.table = table
        self.conn = Connection()
        self.conn.execute(f"DROP TABLE IF EXISTS {table}")
        self.conn.execute(f"CREATE TABLE {table} (id INTEGER PRIMARY KEY, name TEXT)")

    # return the item's name with the id (if any)
    def read(self, id: str | int) -> str | None:
        self.conn.execute(f"SELECT name FROM users WHERE id = {id}")
        result = self.conn.fetch()

        if len(result) == 0:
            return None
        return result[0][0]

    # return the overwritten object (if any)
    def put(self, id: str | int, item: dict[str, str | int]) -> str | None:
        old = self.read(id)
        self.conn.execute(f"INSERT OR REPLACE INTO {self.table} values {item}")
        return old

    # return the deleted item (if any)
    def delete(self, id: str | int) -> str | None:
        self.conn.execute(f"DELETE FROM {self.table} where id = {id}")
        old = self.read(id)
        return old


# SPACING FOR ANSWERS
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# END SPACING

# errors:
# 1. read hardcodes the table
# 2. put doesn't serialize the item correctly
# 3. delete grabs the old value after deleting it
