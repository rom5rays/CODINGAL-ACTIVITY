lower_range = int(input('Enter the lower range:'))
upper_range = int(input('Enter the upper range:'))

for i in range(lower_range, upper_range + 1):
    for j in range(2, i):
        if i%j==0:
            break
    else:
        print(i)