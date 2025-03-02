from typing import TypeAlias

User: TypeAlias = dict[str, str | int]

user_0: User = {
    "id": 0,
    "name": "Name A",
}
user_0_updated: User = {
    "id": 0,
    "Name": "Name A Updated",
}
user_1: User = {
    "id": 1,
    "name": "Name B",
}
user_invalid: User = {
    "_id": 2,
}
