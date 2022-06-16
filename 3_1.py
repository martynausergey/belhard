# Вариант 1
user_text = input("Напечатайте предложение минимум из 3 слов:")
fix_text = "-".join(user_text.split())
print(fix_text)

# Вариант 2
user_text = input("Напечатайте предложение минимум из 3 слов:")
fix_text = user_text.replace(" ", "-")
print(fix_text)