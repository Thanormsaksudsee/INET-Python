from winsound import PlaySound


STR = str(input('Enter a string: '))
lower = (STR.islower())
uper = (STR.isupper())
alpha = (STR.isalpha())
num = (STR.isalnum())



if (STR.isalnum()) == True :
    print('This is what I found about that sthing: ')   
if (STR.islower()) == True :
    print('The letters in the string are all lowercase')
if (STR.isupper()) == True :
    print('The letters in the string are all uppercase')
if (STR.isalpha()) == True :
    print('The string is alplanumeric.')
if (STR.istitle()) == True :
    print('The string contains only digital')
