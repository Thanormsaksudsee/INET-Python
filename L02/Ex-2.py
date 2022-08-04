workedhours = float(input('Enter the numver of hours worked: '))
payrate = float(input("Enter the hourly pay rate: "))

OT = workedhours - 40

if workedhours > 40:
    Overworked = (40*payrate)+(OT*(1.5*payrate))
    print('The gross pay is ${:,.2f} ' .format(Overworked))
else :
    worked = workedhours * payrate
    print('The gross pay is ${:,.2f} ' .format(worked))

                          