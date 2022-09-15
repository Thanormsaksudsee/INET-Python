shop = input('กรอกรหัสสินค้าง :')
price = int(input('ราคาสินค้า :'))
num = int(input('จำนวนสินค้า :'))

total1 = price*num

if shop[1] == '1' :
    total2 = total1 * 0.03
    totalprice = total1 - total2
    print('ราคารวมทั้งหมด : ',format(totalprice ,',.2f'),'บาท')
elif shop[1] == '2' : 
    if num >= 3:
        total2 = total1 * 0.05
        totalprice = total1 - total2
        print('ราคารวมทั้งหมด : ',format(totalprice ,',.2f'),'บาท')
    else :
        total2 = total1 * 0.03
        totalprice = total1 - total2
        print('ราคารวมทั้งหมด : ',format(totalprice ,',.2f'),'บาท')    
else :
    print('ราคารวมทั้งหมด : ',format(total1 , ',.2f'), 'บาท
    