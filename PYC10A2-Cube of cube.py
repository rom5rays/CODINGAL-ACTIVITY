num_to_check = int(input('Enter a number to check:'))

def find_cube(num):
    return num**3

def if_divisible(num):
    if num%3==0:
        return f'The cube of {num} is {find_cube(num)}'
    else:
        return f'The number {num} is not divisible by 3'
    
print(if_divisible(num_to_check))