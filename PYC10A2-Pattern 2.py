rows = int(input('Enter number of rows:'))
num =0
for i in range(1,rows):
    for j in range(1, i+1):
        num +=1
        print( num , end=' ')
    print()