num1 = int(input('Enter a number:'))
num2 = int(input('Enter a number'))

print(
    'Select your choice: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division\n'
)

choice = int(input('Enter a choice in between 1,2,3 and 4:'))

def add_num():
    return 'The sum of the two numbers is:', num1+num2

def sub_num():
    return 'The sum of the two numbers is:', num1-num2

def prod_num():
    return 'The sum of the two numbers is:', num1*num2

def div_num():
    return 'The sum of the two numbers is:', num1/num2

if choice == 1:
    print(add_num())

elif choice == 2:
    print(sub_num())

elif choice == 3:
    print(prod_num())

elif choice == 4:
    print(div_num())

else:
    print('Invalid input')