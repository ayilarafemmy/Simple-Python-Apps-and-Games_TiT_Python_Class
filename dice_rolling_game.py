import random

while True:
 choice = input('Roll the dice?(y/n): ')
 if choice =='y':
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f'({die1}, {die2})')
 elif choice =='n':
    print('thanks for playing the dice game')
    break
 else:
    print('please enter y or n - invalid choice!')

#if the user enters y
# generate 2 random numbers
#print them
# if the user enters n
#Print thank you message
#then terminate
#else
#print invalid choice
