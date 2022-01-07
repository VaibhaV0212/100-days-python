import random

''' Calculate Average height '''
# students = input('Enter students heights = ').split()
# print(students)

# new_list = []
# for i in students:
#     new_list.append(int(i))

# # avg = sum(new_list)
# # print(avg/len(new_list)) 

# total_heights = 0
# for i in new_list:
#     total_heights += i
# print(total_heights)

# # NOW Calculate the length using for loop
# total_length = 0
# for i in new_list:
#     total_length += 1
# print(total_length)

# avg = total_heights/total_length
# print(round(avg,2))


''' Highest Score '''
# score = input('Enter scores = ').split()

# max_score = int(score[0])               
# for i in score:                                  
#     if max_score < int(i):       
#         max_score = int(i)
# print('Higest score =',max_score)


''' Sum of even numbers '''
even = 0
for i in range(1,6):
    if i %2==0:
        even += i
# print(even)        


''' FizzBuzz '''
# for i in range(1,100):
#     if i%3==0 and i%5==0:
#         print(i,'FizzBuzz')
#     elif i%3==0 and i%5!=0:
#         print(i,'Fizz')
#     elif i%3!=0 and i%5==0:
#         print(i,'Buzz')
#     else:
#         print(i)


''' Random Passwork Generator '''

name = input('May I know your name? ')
print(f'Welcome {name} to the Password Generator Site!')
letters_stack = ['A','B','C','D','E','F','G','H','a','b','c','d','e','f','g','h']
symbols_stack = ['{','}','(',')','*','&','^','%','$','#','@','!']
number_stack = ['1','2','3','4','5','6','7','8','9','0']
letters = int(input('How many letters you want? '))
symbols = int(input('How many symbols you want? '))
number = int(input('How many number you want? '))


new_stack_letters = random.choices(letters_stack, k=letters) 
new_stack_symbols = random.choices(symbols_stack, k=symbols)
new_stack_number = random.choices(number_stack, k=number)

final = (new_stack_letters + new_stack_number + new_stack_symbols)
final2 = ''.join(map(str,final))
random.shuffle(final2)
print(f'Your password is = " {final2} "')
# print(type(final2))
