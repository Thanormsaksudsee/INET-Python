'''def Bigkuma():

    hours = int(input('How many hour did you work? '))
    payRate = float(input('Enter your hourly pat rate: ' ))
    grossPay =hours * payRate
    print('Gross pay: $', format(grossPay, ',.2f'), sep='')

Bigkuma()'''


'''try:
    hours = int(input('How many hour did you work? '))
    payRate = float(input('Enter your hourly pat rate: ' ))
    grossPay =hours * payRate
    print('Gross pay: $', format(grossPay, ',.2f'), sep='')
except ValueError:
    print('ERROR: Hours worked and hourly pay rate must')
    print('be valid integers.')'''



try:
    hours = int(input('How many hour did you work? '))

    
    payRate = float(input('Enter your hourly pat rate: ' ))
    grossPay =hours * payRate
    
    print('Gross pay: $', format(grossPay, ',.2f'), sep='')

except ValueError as err:
    
    print(err)