import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
length = int(input("Length: "))
password = ""

for i in range(length):
    password += random.choice(letters)

print(password)