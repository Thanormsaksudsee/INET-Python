def getName():
    first = input('Endter your first name: ')
    last = input('Endter your last name: ')
    return first, last

firstName, lastName = getName()
print('First name :',firstName,' Last name :', lastName)