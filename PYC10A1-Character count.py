word = input('Enter the word:').lower()
char = input('Enter the character to check:').lower()
count = 0

for i in word:
    if i==char:
        count +=1
print(f'The character {char} appears {count} times in the {word}')