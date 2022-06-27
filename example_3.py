#Вывести где не т email'а
users = {
    1: {
        "name": "name",
        "email": "info@info.com"
    },
    2: {
        "name": "name2",
        "email": ""
    },
    3: {
        "name": "name 3"
    }
}
for user in users.values():
    if "email" not in user:
        print(user["name"])
    elif not user ["email"]:
        print(user["name"])
