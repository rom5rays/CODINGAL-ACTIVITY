n = int(input('Enter a number to find the factorial of:'))

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
    
print(f'The factorial of {n} is {factorial(n)}')