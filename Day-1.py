'''
The input() will get user input in console
the print() will print the "Hello" and the user input 
'''

# print('Day 1 = String Manpulation')
# print('String Manipulation is done using "+" sign.')
# print('e.g print("Hello" + "World")')
# print('New lines of code can be created with a backlash and n')

'''
Printing the 'name' with 'Hi' msg in below code.
'''
# print('Hiii ' + input('Enter your name? '))

'''
Taking user name and pet name to generate Rock Band name.
'''
# print('Welcome to the Band Name Generator!')
# name = input('Enter your name?\n')
# pet = input("Enter your pet's name?\n")
# # print('Your band name can be {0} {1}'.format(name,pet))
# print(f'Your name can be {name} {pet}')


''' Printing the length of function'''
# name_length = input('Enter your name? ')
# print(len(name_length))

'''Taking user input: Method-1'''
# a,b = input('Enter two values=').split()
# print('Value of a {} and b {}'.format(a,b))


'''Taking multiple user input in single line: Method-2'''
# x = [int(x) for x in input('Enter values in list = ').split()]
# print(x)

''' Inter-changing variable values'''
a,b = input('Enter 2 values=').split()
print('Original values {} and {}'.format(a,b))
a,b = b,a
print(f'After interchanging- {a} and {b}')