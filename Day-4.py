import random
import numpy as np

# GENERATE RANDOM WHOLE NUMBERS
a = random.randint(1,9)
# print(a)

# GENERATE RANDOM Floating NUMBERS - [0,1) where 1 is not included
b = random.random()
# print(b)

''' HEAD & TAIL '''
# random_side = random.randint(0,1)
# if random_side == 1:  print('Heads')
# else: print('Tails')

''' Create a LIST and pick a random person to buy a meal '''
persons = ['Dolli','Nids','Vaibhav','Mahak']
total_people = len(persons)

#  random.choice()

buy_meal = random.randint(0, total_people-1)
# print(buy_meal)
final_buyer = persons[buy_meal]
# print(f'{final_buyer} is buying us meal!')

''' Treasure hunt '''
# row1 = ['A','B','C']
# row2 = ['D','E','F']
# row3 = ['G','H','I']

# row4 = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# # print(row4[0][1])
# position = input('Where do You want you "X" now? First enter row and then column = ')
# hori = int(position[0])
# ver = int(position[1])
# row4[hori][ver] = 'X'
# print(f"{row1}\n{row2}\n{row3}")


'''  ROCK PAPER SCISSOR '''
player = int(input('Choose 0 for Rock, 1 for Paper, 2 for Scissor = '))
computer = random.choice(np.arange(0,3))
# print(player, computer)

if player >=3 or player<=0:
    print('Invalid entry!')
elif player == 0 and computer ==2:
    print('You win!')
elif player == 0 and computer ==1:
    print('You lose!')
elif player ==1 and computer==0:
    print('You Win!')
elif player == 1 and computer==2:
    print('You lose!')
elif player == 2 and computer==0:
    print('You lose!')
elif player==2 and computer==1:
    print('You win!')
elif player==computer:
    print('Tie') 



