import random

number_to_guess = random.randint(1, 3)

while True:
    try:
        guess = int(input('Guess a number between 1 and 3: '))

        if guess < number_to_guess:
            print('too low')
        elif guess > number_to_guess:
            print('too high')
        else:
            print('good job, you guessed the number!')
            break

    except ValueError:
        print('please enter a valid number!')
