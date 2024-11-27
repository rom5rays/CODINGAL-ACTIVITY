num = int(input('Enter a number:'))

digits = 0

while num>0:
    digits += 1
    num //= 10
print(digits)