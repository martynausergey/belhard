# 1 Вариант
# Вывести первые n чисел, кратные m и больше k
n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
k = int(input("Ввещиье число k: "))
x = k
count = 0
while count != n:
	if not x % m and x > k:
		print(x)
		count += 1
	x += 1
# 2 Вариант 
n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
k = int(input("Ввещиье число k: "))
x = k
count = 0
while count < 0:
	if not x % m:
		count += 1
		print(i)
	i += 1
