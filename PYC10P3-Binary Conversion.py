num = int(input('Enter a number:'))

binary = ''

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num //= 2

print(binary)
