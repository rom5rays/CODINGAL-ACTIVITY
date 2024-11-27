num = int(input('Enter a number: '))
num_to_check = num

sum = 0
digit = 0
i = 0

while (num>0):
    digit = num%10
    sum += digit**3
    num //= 10

if num_to_check == sum:
    print(f'{num_to_check} is a Armstrong number')
else:
    print(f'{num_to_check} is not Armstrong number')