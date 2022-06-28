number = int(input())
def binary(n):
    binary_n = ""
    while n > 0:
        binary_n = str(n % 2) + binary_n
        n = n // 2
    return binary_n
    return number
print(binary(number))
print(number)
