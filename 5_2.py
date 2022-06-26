a = int(input("Введите число a: "))
while not a.isdigit():
	a = int(input("Не является числом. Введите число: "))
	a = int(a)
q = input("Введите действие (+, -, *, /, **): ")
b = int(input("Введите число b: "))
while not b.isdigit():
	b = int(input("Не является числом. Введите число: "))
	b = int(b)
if q == "+":
	result = a + b
elif q== "-":
	result = a - b
elif q == "*":
	result = a * b
elif q == "/":
	result = a / b
elif q == "**":
	result == a ** b
else:
	result = a % b
print("Результат :", result)
