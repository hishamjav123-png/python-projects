binary = input("Enter a binary number: ")

decimal = int(binary, 2)
hexa = hex(decimal)

print("Hexadecimal:", hexa[2:].upper())