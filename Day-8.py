''' Calc the Area to be painted '''
# height = float(input('Height of wall = '))
# width = float(input('Width of wall = '))
# coverage = 5

# def paint_calc(h=height, w=width, c = coverage):
#     return (h*w)/c

# cans = paint_calc(height,width)
# print(round(cans))

''' Cipher msg '''
# alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
# 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# dir = input('Type "encode" to encode and "decode" to decode = ').lower()
# text = input('Type your msg here = ').lower()
# shift = int(input('Enter no. of shifts = '))

# def encrupt(plain_text, shift_amount):
#     cipher_text = ""
#     for i in plain_text:
#         position = alphabets.index(i)
#         new_position = position + shift_amount
#         cipher_text += alphabets[new_position]
#     print(f'The encoded text is {cipher_text}')

# def decrypt(plain_text, shift_amount):
#     original_text = ""
#     for i in plain_text:
#         position = alphabets.index(i)
#         new_position = position - shift_amount
#         original_text += alphabets[new_position]
#     print(f'The decoded text is {original_text}')

# repeat = False

# if dir == 'encode':
#     encrupt(plain_text = text,shift_amount = shift)
# elif dir == 'decode':
#     decrypt(plain_text = text,shift_amount = shift)
# else:
#     print('Wrong INPUT')  

''' Modifying the cipher msg code '''



def caesar(start_text, shift_amount, cipher_direction):
    
    end_text = ""
    
    if cipher_direction == 'decode':
        shift_amount *= -1
            
    for char in start_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_amount
            end_text += alphabets[new_position]
        else:
            end_text += char
    print(f'The {dir}d msg  is {end_text}')


alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

should_continue = True
while should_continue:
    dir = input('Type "encode" to encode and "decode" to decode = ').lower()
    text = input('Type your msg here = ').lower()
    shift = int(input('Enter no. of shifts = '))

    shift = shift % 26

    caesar(start_text = text, cipher_direction=dir, shift_amount=shift)

    result = input('Do you wish to continue? Yes / No = ').lower()
    if result == 'no':
        should_continue = False
        print('Thanks for using!')
        


