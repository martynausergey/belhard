# Вывести четные числа от 2 до n по 5 в строку
n = int(input("Введите n: "))
for i in range(2, n + 1, 2):
    print(i, end=" ")
    if i % 5 == 0:
        print("")

# Вариант 2
n = int(input("")
count = 0
for i in range(2, n + 1, 2):
    if count < 5:
        print(i, end="")
        count += 1
    else:
        print(i)
        count = 1
# Вариант 3
n = int(input("")
count = 0
for i in range(2, n + 1, 10):
        for j in range(i, i + 9, 2):
            if j <= n:
                print(j, end=" ")
            else:
                break
        print()
        
