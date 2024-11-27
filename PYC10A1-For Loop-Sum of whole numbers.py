num = int(input('Enter the number up to which you want the sum:'))

sum = 0

for i in range(1, num + 1):
    sum += i
print(f'The sum of numbers from 1 to {num} is: {sum}')
