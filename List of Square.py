def Squared_Values(start, end):
    lst = []

    for i in range(start, end):
        lst.append(i**2)

    lst_even = []
    lst_odd = []

    for i in lst:
        if i%2 == 0:
            lst_even.append(i)
        else:
            lst_odd.append(i)
    print(lst_even)
    print(lst_odd)

square_num = Squared_Values(1,5)
print(square_num)
