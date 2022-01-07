''' Guess checker '''
import random
# words_list = ['nids','vaib','pagal']
# print(f'Word list is {words_list}')
# comp_pick = random.choice(words_list)
# guess = input('Enter a letter = ').lower()
# # print(guess)
# if guess in comp_pick:
#     print('You guessed it right!')
#     print(f'Computer picked {comp_pick}')
# else:
#     print('Wrong ans')
#     print(f'Computer picked {comp_pick}')

''' Replacing word with _ '''
words_list = ['nids','vaib','pagal']
print(f'Word list is {words_list}')
comp_pick = random.choice(words_list)
print(f'Computer picked {comp_pick}')
display = []
for i in comp_pick:
    i = '_'
    display.append(i)

end_of_game = False
lives = 3
while not end_of_game:
    guess = input('Enter a letter = ').lower()

    for i in range(len(comp_pick)):
        letter = comp_pick[i]
        if letter == guess:
            display[i] = letter
    if guess not in comp_pick:
        lives = lives-1
        if lives == 0:
            print('You lose!')
            end_of_game = True
        
    print(display)

    if "_" not in display:
        end_of_game = True
        print('You Win!')
   
        

# print(f'Computer picked {comp_pick}')


