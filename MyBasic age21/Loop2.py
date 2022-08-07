KeepGoing = 'n'

while KeepGoing == 'n' :
    sales = float(input('Enter the amount of sales: '))
    CommRate = float(input('Enter the commission rate: '))
    
    commission = sales * CommRate
    
    print('the commission is $', \
    format(commission, ',.2f'),sep='')

    KeepGoing = input('Do you want to calculate anoter' +\
                  'commission (Enter y For yes):')  