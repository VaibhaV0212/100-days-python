''' Black Jack Game '''
import random

is_game_over = False
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    random_card = random.choices(cards, k=2)
    return random_card

def deal_one_card():
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "It's a Draw !!"
    elif computer_score == 0:
        return "Computer Wins with a Blackjack!!"
    elif user_score == 0:
        return "You Win with a Blackjack!!"
    elif user_score > 21:
        return 'You lose, you went over!'
    elif computer_score > 21:
        return 'Computer loses the game!'
    elif user_score > computer_score:
        return f'You Win with high score {user_score}!'
    else:
        return f'Computer wins with high score {computer_score}'
user_cards = deal_card()
computer_cards = deal_card()

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f' Your cards {user_cards} and score is {user_score}')
    print(f" Computer's first card is {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        if input('If you want to draw another cards? y/n :') == 'y':
            user_cards.append(deal_one_card())
            print(user_cards)
        else:
            is_game_over = True
            print(' Thanks for playing! ')

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_one_card())
    computer_score = calculate_score(computer_cards)

print(f'Computer cards are {computer_cards}')
print(compare(user_score,computer_score))