import random

user_move = input('Enter your move\nRock, paper or scissors:').capitalize()

computer_move = random.choice(['Rock', 'Paper', 'Scissors'])

print(f'The computer move is {computer_move}')

if user_move == computer_move:
    print("It's a tie")
elif user_move == 'Rock':
    if computer_move == 'Paper':
        print('The computer won!')
    elif computer_move == 'Scissors':
        print('You won!')
elif user_move == 'Paper':
    if computer_move == 'Rock':
        print('You won!')
    elif computer_move == 'Scissors':
        print('The computer won!')
elif user_move == 'Scissors':
    if computer_move == 'Rock':
        print('The computer won!')
    elif computer_move == 'Paper':
        print('You won!')
else:
    ('Invalid move')
                        