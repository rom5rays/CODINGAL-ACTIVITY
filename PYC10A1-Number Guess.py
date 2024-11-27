import random

user_move = int(input('Enter a number between 1 to 10:'))

computer_move = random.randint(1, 10)

if user_move==computer_move:
    print(f'You won. The computer move was {computer_move}')
else:
    print(f'You lose. The computer move was {computer_move}')