users = int(input("Кол-во новых пользователей: "))
dict = {x: {"Имя пользователя": input(f"{x} Имя пользователя: "),
"Email пользователя": input(f"{x} Email пользователя: ")}
for x in range (1, users + 1)}
print(dict)
