num = input('Enter a number at least 3 digits:')
total_digits = len(num)
product = 1

if total_digits >= 3:
    mid_index = total_digits // 2
    if total_digits % 2 == 0:
        mid_digits = num[mid_index - 1 : mid_index + 1]
    else:
        mid_digits = num[mid_index]

    for i in mid_digits:
        product *= int(i)

    print(f'The product of the mid digits is {product}')

else:
    print('Enter a number with at least 3 digits')
