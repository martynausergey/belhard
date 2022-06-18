user_text = int (input("Введите число №1: "))
plus = 0
min = 0
if(user_text >= 0):
    plus +=  1
    print("Число положительное")
else:
    min += 1
    print("Число отрицательное")
user_text2 = int (input("Введите число №2: "))
if(user_text2 >= 0):
    plus += 1
    print("Число положительное")
else:
    min += 1
    print("Число отрицательное")
user_text3 = int (input("Введите число №3: "))
if(user_text3 >= 0):
    plus += 1
    print("Число положительное")
else:
    min += 1
    print("Число отрицательное")
print("Положительных: ",plus, "\nОтрицательных: ", min)