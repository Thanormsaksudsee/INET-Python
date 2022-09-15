'''.ร้านขายหนังสือร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ ถ้าคุณซื้อหนังสือมากกว่า 3 เล่ม ที่มีมูลค่ารวมเกิน 500 บาท คุณจะได้ส่วนลด 10%

ให้เขียนโปรแกรมรับจำนวนหนังสือที่ซื้อและราคารวม จากนั้นคำนวณราคาที่ต้องจ่าย'''

num = int(input('How many books: '))
price = int(input('How much: '))


if num >= 3 and price >= 500 :
    dis = price*0.10
    dis2 = price-dis
    print('You have to pay ', dis2 ,'bath.')
else:
    print('You have to pay ', price , 'bath.')
