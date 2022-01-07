'''  BMI 2.0 '''

# height = float(input('Enter your height in m= '))
# weight = float(input('Enter your weight in kg= '))
# bmi = weight/height**2
# print(f'your current BMI is {bmi}')

# if bmi>35:
#     print('Go and see a doctor!')
# elif bmi >30 and bmi<35:
#     print('You are obese')
# elif bmi>25 and bmi<30:
#     print('You are over weight')
# else:
#     print('Normal weight!')

'''  Pizza Order calculator '''
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25

# cheese = 1

# bill = 0

# print("Welcome to Vaibhav's hut")
# size = input('Enter the size of pizza? S, M or L =')
# add_pep = input('Do you want pepperoni? Y or N =')
# extra_cheese = input('Want extra cheese? Y or N =')

# if size == 'S':
#     bill += 15
# elif size== 'M':
#     bill +=20
# else:
#     bill +=25

# if add_pep == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == 'Y':
#     bill += 1

# print(f'You total bill is {bill} /-')


''' Treasure Island '''
print("""
Welcome to the Treasure Island\nYour mission is to find the treasure\nYour're are cross road. """)
turn = input("Where do you want to go? 'Left' or 'Right-' ").lower()

if turn == 'Left':
    print('You are at lake. There is an island in the middle of the lake.')
    next_turn = input("Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if next_turn == 'wait':
        boat = input('Which color boat you want? Blue, Green ? ').lower()
        if boat == 'Blue':
            print('Its a Beast room. Game Over.')
        else:
            print('You win.')
    else:
        print('Go ahead and swim and die. Game Over.')
else:
    print("You can't be Right, bcz women's are always Right!")