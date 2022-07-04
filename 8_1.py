n = int(input("Введите глубину: "))


def pascal_triangle(rows):
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]


print(pascal_triangle(n))

