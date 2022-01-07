print('Welcome back Vaibhav!')

'''  Entering a value say 86 and result should be 8 + 6 = 14  '''
# num = int(input('Enter a num='))
# new_num = str(num)
# print(int(new_num[0]) + int(new_num[1]))


'''  Life calculator '''
# age = int(input('Enter your age= '))
# days = (90*365) - (age*365)
# month = (90*12) - (age*12)
# weeks = (90*52) - (age*52)
# print(f'You have {month} months, {weeks} weeks and {days} days left! Do Enjoy!')


'''  Tip calculator '''

print('Welcome to the Tip Calculator')
bill = float(input('What was the total bill? '))
tip = int(input('What percentage tip you would like to give? 10 , 12 or 15? '))
tip_amt = float(bill)* float(tip/100)
final_bill = tip_amt + bill
# print(final_bill)
person_split = int(input('How many people to split the bill? '))
per_pay = final_bill//person_split
print(f'Each person to pay {per_pay}')