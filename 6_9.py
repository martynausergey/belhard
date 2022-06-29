#Вывести где нет email'а
users = {
    1: {
        "name": "Костя",
        "lname": "Шило",
        "number": "1998",
        "email": "info@info.com"
    },
    2: {
        "name": "Вася",
        "lname": "Горох",
        "number": "1488",
        "email": ""
    },
    3: {
        "name": "Петя",
        "lname": "Яйцо",
        "number": "1337",
    }
}
for user in users.values():
    if "email" not in user:
        print(user["name"])
    elif not user ["email"]:
        print(user["name"])

