name = input('Enter your name = ')
print('Types of Photo')
print('1. One inch')
print('2. Two inch')
print('3. Polaroid')
select = int(input('Select type = '))
amount = int(input('Enter amount = '))

if select == 1:
    #โหลละ65
    if amount <= 3 :
        print('Your name is ', name)
        print('Type of photo is One inch')
        print('Amount is ', amount)
        total = 65*amount
        print('Total price is 65*%d = %d' %(amount,total))
    else :
    #ลด5%
        print('Your name is ', name)
        print('Type of photo is One inch')
        print('Amount is ', amount)
        total = (65*amount)
        valsher = total*0.05
        total2 = total-valsher
        print('Total price is 65*%d = %.2f' %(amount,total2))
if select == 2:
    #โหลละ80
    if amount <= 3 :
        print('Your name is ', name)
        print('Type of photo is Two inch')
        print('Amount is ', amount)
        total = 80*amount
        print('Total price is 80*%d = %d' %(amount,total))
    else :
    #ลด5%
        print('Your name is ', name)
        print('Type of photo is Two inch')
        print('Amount is ', amount)
        total = (80*amount)
        valsher = total*0.05
        total2 = total-valsher
        print('Total price is 80*%d = %.2f' %(amount,total2))
if select == 3:
    print('Your name is ', name)
    print('Type of photo is polaroid')
    print('Amount is ', amount)
    total = 70*amount
    print('Total price is 70*%d = %d' %(amount,total))