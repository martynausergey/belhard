message = input("Сообщение: ")
key = input("Ключ: ")
if len(message) != len(key):
    raise ValueError("len of message and key must be equal")
message_bin = ""
key_bin = ""
for i in range(len(key)):
    char = bin(ord(message[i]))[2:]
    char = "0" * (8 - len(char)) + char
    message_bin += char
    char = bin(ord(key_bin[i]))[2:]
    char = "0" * (8 - len(char)) + char
    key_bin += char
result = ""
for i in range(len(key_bin)):
    if message_bin[i] !=key_bin
        result += "1"
    else:
        result += "0"
print(message_bin)
print(key_bin)