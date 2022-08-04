Hoursworked = float(input('Enter the number of Hours worked : '))
payrate = float(input('Enter the hourly pay rate : '))

Thegrosspayhoursworked  = Hoursworked*payrate
HoursworkedOT  = (40*payrate)+(Hoursworked-40*(1.5*payrate))

if Hoursworked > 40:
    print('The gross pay hours worked is $' ,Thegrosspayhoursworked )
else :
    print('The gross pay hours worked is $' ,HoursworkedOT )

