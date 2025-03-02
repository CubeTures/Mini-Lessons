from src.v0 import CRUD

# 1. does your testing look like this? what issues could writing tests like this cause?
# 2. you'd have to go out of your way to run this file just to test the validity of your code
# 3. you have to visually inspect the output for discrepancies
# 4. an error prevents other tests from running
# 5. you have to comment out a test while its function is temporarily being edited
# 6. state management between tests is a hassle
# 7. many more issues
if __name__ == "__main__":
    db = CRUD("tests")

    # models
    item_a: dict[str, str | int] = {"id": 0, "name": "Name A"}
    item_a_updated: dict[str, str | int] = {"id": 0, "name": "Name A Updated"}
    item_b: dict[str, str | int] = {"id": 1, "name": "Name B"}
    item_c: dict[str, str | int] = {"id": 2, "name": "Name C"}

    print("===== Loading Data =====")
    db.put(item_a["id"], item_a)
    db.put(item_b["id"], item_b)

    print("===== Test Read =====")
    print("ID should be 0:", db.read(item_a["id"]))
    print("None should be returned:", db.read(item_c["id"]))

    print("===== Test Put =====")
    ##### CURRENTLY BROKEN
    # old = db.put(item_a_updated["id"], item_a_updated)
    # print(item_a, "==", old)
    # old = db.put(item_c["id"], item_c)
    # print("Should be None:", old)

    print("===== Test Delete =====")
    old = db.delete(item_c["id"])
    print(item_c, "==", old)
    old = db.delete(item_c["id"])
    print("Should be None:", old)
