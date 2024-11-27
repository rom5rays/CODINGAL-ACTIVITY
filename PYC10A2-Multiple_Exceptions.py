try:
    num1,num2 = eval(input('Enter two numbers separated by comma:'))
    result = num1/num2
    print(f'The division of the two numbers is {result}')

except ZeroDivisionError:
    print('Division by zero is not possible')

except SyntaxError:
    print('Commas missing. Enter the numbers separated by commas like 1,2,3:')

except:
    print('Wrong input.')

else:
    print('No exception')