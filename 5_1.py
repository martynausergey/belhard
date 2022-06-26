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
