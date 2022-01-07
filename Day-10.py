''' Functions''' 

def format_name(f_name, l_name):
    result = f_name + ' ' + l_name
    return result.title()

# print(format_name('vai', 'nids'))

''' Days in month '''

def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def days_to_month(year, month):
    result = leap(year)
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month > 12 and month < 1:
        return 'Invalid Input'

    if result and month == 2 :
        return 29
    return month_days[month - 1]    

# year = int(input('Enter the year : '))
# month = int(input('Enter the month : '))
# days = days_to_month(year, month)
# print(days)


''' Calculator  '''
def add(n1, n2):
    return n1 + n2
 
def subtract(n1, n2):
    return n1 - n2
 
def multiply(n1, n2):
    return n1 * n2
 
def divide(n1, n2):
    return n1 / n2

operations = {'+': add , '-': subtract, '*': multiply, '/' : divide}
num1 = float(input('Enter a number : '))
for ops in operations:
    print(ops)

should_continue = True
while should_continue:
    todo = input('Which operation you want to perform? ')
    num2 = float(input('Enter next number : '))
    
    calculation_function = operations[todo]
    final_result = calculation_function(num1, num2)
    print(f'{num1} {todo} {num2} = {final_result}')
    if input(f"type 'y' to continue calculating with {final_result} or type 'n' to exit : ") == 'y':
        num1 = final_result
    else:
       should_continue = False
       print('Thanks!!')