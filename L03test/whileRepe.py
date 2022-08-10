keep_going = 'y'

while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    com_rate = float(input('Enter rhe cmmission rate:  '))
    commission = sales * com_rate
    print('The commission is $' , format(commission, ',.2f'))
    
    keep_going = input('Do you want to calculate another' + \
                       'commission (Enrer y for yes):')