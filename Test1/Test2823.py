'''คำนวนรูป1นิิ้วหรือ2นิว้ อินพุต คีบอด ได้แก่ ชื่อ ชนิดรูป1หรือ2นิ้วหรือโพลาลอย และจำนวนสั่ง'''

name = input('Enter your name : ')
print('Types of Photo\n1. One inch\n2. Two inch\n3. Polaroid')

select = int(input('Select type ='))
amount = int(input('Endter amount ='))

if  select == 1:
    if  amount < 3:
        price = 65*amount
        print('Your name is ' ,name)
        print('Type of photo is One inch')
        print('Amount is ',amount)
        print('Total price is  65*%d = %d'%(amount,price))
    elif  amount >= 3:
        price = 65*amount
        discout = 65 * 0.05 * amount
        net = price-discout
        print('Your name is ' ,name)
        print('Type of photo is One inch')
        print('Amount is ',amount)
        print('Total price is  65*%d = %d'%(amount,price))
        print('Discount', discout)
        print('Net price', net)    
if  select == 2:
    if  amount < 3:
        price = 80*amount
        print('Your name is ' ,name)
        print('Type of photo is Two inch')
        print('Amount is ',amount)
        print('Total price is  80*%d = %d'%(amount,price))

    elif  amount >= 3:
        price = 80*amount
        discout = 80 * 0.05 * amount
        net = price-discout
        print('Your name is ' ,name)
        print('Type of photo is Two inch')
        print('Amount is ',amount)
        print('Total price is  80*%d = %d'%(amount,price))
        print('Discount', discout)
        print('Net price', net)    
if  select == 3:
    if  amount < 3:
        price = 70*amount
        print('Your name is ' ,name)
        print('Type of photo is Polaroid')
        print('Amount is ',amount)
        print('Total price is  70*%d = %d'%(amount,price))



