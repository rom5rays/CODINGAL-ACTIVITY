base = int(input('Enter a number for base: '))
power = int(input('Enter a number for power: '))

exponent = 1

for i in range(1, power+1):
    exponent *= base
print(exponent)


