''' Number Guessing '''

import random 

EASY_LEVEL = 5
HARD_LEVEL = 3
comp_guess = random.randint(1,100)

def num_guessing(num, turns):
    if num == comp_guess:
        print(f'You got it! The answer is {comp_guess}')
    elif num > comp_guess:
        print('Guess too high!')
        return turns - 1
    elif num < comp_guess:
        print('Guess too Low!')  
        return turns - 1           
    

def set_diffuculty():
    choice = input("Choose a diffuculty. Type 'easy' or 'hard' : ")
    if choice == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print('Welcome to the number guessing game!')
    print('Think of a number between 1 & 100.')
      
    turns = set_diffuculty()            # local variable
    
    guess = 0
    while guess != comp_guess:
        print('Remaining guess : ', turns)
        guess = int(input('Make a guess : '))
        turns = num_guessing(guess, turns)
        if turns == 0:
            print(f"Out of turns!! Correct answer is {comp_guess}" )
            return

game()




