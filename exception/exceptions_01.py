import exception

try:
    first_number = int(input('Enter your first_number : '))
    second_number = int(input('Enter your second_number : '))
    result = first_number / second_number
    print('The result = ', result)
except ValueError as err_msg:
    print('Please Enter only numbers not text', err_msg)
except ZeroDivisionError as err_msg:
    print('Cannot divide By Zero - take Care !!', err_msg)
except exception as err_msg:
    print('Error happend - Please contact administrator at 01231231212', err_msg)
finally:
    print('This is finally statement - executed any time')
print('Continue or End of The program')
