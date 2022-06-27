#Запрашивает число, пока буквы - просит еще раз
users = input("Число")
while not users.isdigit():
    users = input("Число, идиот!!!")
