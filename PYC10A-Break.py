test_str = input('Enter the string to check:').upper()
found = False

for char in test_str:
    if char == 'A':
        found = True
        break
if found:
    print(f'Character A is found in {test_str.capitalize()}')       
else:
    print(f'Character A is not found in {test_str.capitalize()}')