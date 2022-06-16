# 1
name = input("Имя - ")
age = input("Возраст - ")
city = input("Город - ")
print(f"Добрый день {name}! Тебе {age} года. Ты из города {city}")

# 2
name = input("Имя - ")
age = input("Возраст - ")
city: str = input("Город - ")
print("Добрый день {}! Тебе {} года. Ты из города {}".format(name, age, city))

# 3
name = input("Имя - ")
age = input("Возраст - ")
city = input("Город - ")
print("Добрый день %s. Тебе %d года. Ты из города %s." % (name, age, city))



