L = [4, 5, 1, 2, 9, 7, 10, 8]
print('Original List:', L)

count = 0

for i in L:
    count += 1
print(count)

avg = count/len(L)
print(avg)

L.sort()
print(L)

print(L[0])

print(L[-1])