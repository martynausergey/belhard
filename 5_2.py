while True:
	a = input("Введите число a: ")
	while not a.isdigit():
		a = input("Не является числом. Введите число: ")
	a = int(a)
	q = input("Введите действие (+, -, *, /, **): ")
	list_q = ["+", "-", "*", "/", "**"]
	while q not in list_q:
		q = input("Неправильное действие, введите заново: ")
	b = input("Введите число b: ")
	while not b.isdigit():
		b = input("Не является числом. Введите число: ")
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
	print("Результат :", result)
