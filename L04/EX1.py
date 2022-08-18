First = str(input('Enter your first name: '))
Last = str(input('Enter your lasst name: '))
ID = (input('Enter your student ID number: '))
total = First[:3]+Last[:3]+ID[-3:]
print('You system login name is: ',total)
print('You system login name is: ',First[:3]+Last[:3]+ID[-3:])



