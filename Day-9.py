''' Dictionaries ''' 

students_score = {
    'Harry' : 91,
    'Sidd'  : 86,
    'Shakuntala' : 67,
    'Raj' : 44
}

students_grade = {}

for students in students_score:
    # print(students)
    score = students_score[students]
    if score > 90:
        students_grade[students] = 'Outstanding'
    elif score > 80:
        students_grade[students] = 'Very good'
    else:
        students_grade[students] = 'Fail'
# print(students_grade)

''' Travel log - make a new function to add a new country, no. of times vistied and places also. '''
travel_log = [
    {
        "country" : "France",
        "visits" : 4,
        "cities" : ["Paris","Lille","Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 12,
        "cities" : ["Berlin","Hanburg","Stuttgart"]
    },
]

def add_new_country(country_visited, times_visted, cities_visited):
    new_country ={}
    new_country['country'] = country_visited
    new_country['visits'] = times_visted
    new_country['cities'] = cities_visited
    travel_log.append(new_country)
    
add_new_country('Russia', 2, ['Moscow','Saint Petersburg'])
# print(travel_log)

''' Auction program '''
from replit import clear

bidders = {}

def higest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for i in bidding_record: 
        bid_amount = bidding_record[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f'Maximum auction is {highest_bid} by {winner}')

should_continue = True
while should_continue:
    print('Welcome to the secret auction program!')
    name = input("What's your name? ")
    bid = float(input("What's your bid? "))
    bidders[name] = bid
    result = input('Are there any other bidders? yes/no ? ').lower()
    if result == 'yes':
        clear()
    elif result == 'no':
        should_continue = False
        higest_bidder(bidders)
        
