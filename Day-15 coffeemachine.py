MENU = {
    "espresso": {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.5
    },
    "latte": {
        "ingredients" : {
            "water" : 200,
            "milk": 150,
            "coffee" : 24,
        },
        "cost" : 2.5
    },
    "cappuccino": {
        "ingredients" : {
            "water" : 250,
            "milk":100,
            "coffee" : 24,
        },
        "cost" : 3.0
    }
}

profit = 0
resources = {
    "water":300,
    "milk":200,
    "coffee":100
}


def make_coffee(drink_name, order_ingredients):
    '''Deduct the required ingredients from the resources'''
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f'Here is your {drink_name}. Enjoy!')



def is_transaction_successful(money_received, drink_cost):
    '''Returns True when the payment is accepted'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f'Here is the ${change} is change.')
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry thats not money!')
        return False

def is_resource_sufficient(order_ingredients):
    '''Returns True when order can be made, False if not.'''
    is_enough = True
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print(f'Sorry there is not enough {i}')
            is_enough = False
    return is_enough


def process_coins():
    '''Returns the total calculated from the coins inserted.'''
    print('Please insert coins!')
    total = int(input('How many quaters? ')) * 0.25
    total += int(input('How many dines? ')) * 0.1
    total += int(input('How many nickles? ')) * 0.05
    total += int(input('How many pennies? ')) * 0.01
    return total

is_on = True
while is_on :
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        # print(f'hello {profit}' )
        print(f"Water: {resources['water']} ml")
        print(f"Milk:  {resources['milk']} ml")
        print(f"Coffee:  {resources['coffee']} g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        # print(drink['ingredients'])
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])


