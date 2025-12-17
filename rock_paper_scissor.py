import random

emojis = {'r': '👊🏿👊', 'p': '📜📃', 's': '✂️✂️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('Rock, paper or scissor? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('invalid choice - what you chose is not correct')

def display_choices(user_choice, computer_choice):
    print(f'Computer chose {emojis[computer_choice]}')
    print(f'You chose {emojis[user_choice]}')

def determine_winner(user_choice, computer_choice):
    if computer_choice == user_choice:
        print('Tie! - no winner')
    elif ((computer_choice == 's' and user_choice == 'r') or
          (computer_choice == 'p' and user_choice == 's') or
          (computer_choice == 'r' and user_choice == 'p')):
        print('You win!, computer lose!')
    else:
        print('Computer wins!, You lose!')

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        should_continue = input('Do you want to Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()
