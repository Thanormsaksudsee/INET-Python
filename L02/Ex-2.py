
workedhours = float(input('Enter the number of hours worked: '))
payrate = float(input("Enter the hourly pay rate: "))

OT = workedhours - 40

if workedhours > 40:
    ss = (40*payrate)+(OT*(1.5*payrate))
   
else :
    ss = workedhours * payrate
    
print('The gross pay is ${:,.2f} ' .format(ss))

                          