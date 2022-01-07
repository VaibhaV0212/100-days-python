''' Higher and Lower Game '''

import random
from replit import clear

score = 0
data = [
    {
        'name' : 'Dolli',
        'follower_count' : 734,
        'desc' : 'Java Player',
        'country' : 'Garahkota' 
    },
    {
        'name' : 'Nids',
        'follower_count' : 871,
        'desc' : 'ML Player',
        'country' : 'US' 
    },
    {
        'name' : 'Mahak',
        'follower_count' : 634,
        'desc' : 'SQL Player',
        'country' : 'Sri Lanka' 
    },
    {
        'name' : 'VaibhaV',
        'follower_count' : 1234,
        'desc' : 'Python Player',
        'country' : 'India' 
    },
]

def format_data(account):
    '''Format the account data into printable formats'''
    account_name = account['name']
    account_desc = account['desc']
    account_country = account['country']
    return f"{account_name}, a {account_desc} from {account_country}"

def check_answer(guess, a_followers,b_followers):
    # Use the if stmnt to check wheater the user is correct or not.
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
            
B = random.choice(data)
# Make code repeatble:
should_continue = True
while should_continue:
    # Generate a random account from the data.
    A = B
    B = random.choice(data)
    while A == B:
        B = random.choice(data)

    print(f'Compare A: {format_data(A)}')
    print(f'Against B: {format_data(B)}')

    # ASk the user there choice.
    guess = input(f'Who will win, A or B ? = ').lower()

    # Compare the followers of A and B.
    a_followers = A['follower_count']
    b_followers = B['follower_count']

    is_correct = check_answer(guess,a_followers,b_followers)

    # Clear the screen.
    # clear()

    # Give feedback and score
    if is_correct:
        score += 1
        print('You are correct and score is ', score)
    else:
        should_continue = False
        print('You are wrong and score is ', score)


    














''' Random Try '''
# score = 0
# players = {}
# players['VaibhaV'] = 100
# players['Nids'] = 200
# players['Dolli'] = 400
# players['Mahak'] = 390
# a = players.items()

# random_players = random.sample(list(a), k=2)
# A = random_players[0][0]
# B = random_players[1][0]
# A1 = random_players[0][1]
# B1 = random_players[1][1]
# # print(A, B, player1, player2)

# def play(choose):
#     if A1 > B1:
#         print(f'{A} wins by',A1)
#     else:
#         print(f'{B} wins = ', B1)

# should_continue = False
# while not should_continue:
#     choose = input(f'The competition is between {A} vs {B}. On whom will you bet? {A} or "{B} ? ').lower()
#     play(choose)

    
# should_continue=True