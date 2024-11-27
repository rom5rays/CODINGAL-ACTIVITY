prefer_range = int(input('Enter a number to satisfy the prefer range (>15):'))

if prefer_range >=15:
    for i in range(1, prefer_range + 1):
        if i%20==0:
            print('twist')
        elif i%15==0:
            pass
        elif i%5==0:
            print('fizz')
        elif i%3==0:
            print('buzz')
        else:
            print(i)
else:
    print('The range should be at least 15 or greater')