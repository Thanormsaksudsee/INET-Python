print('ระบุขอมูลสินค้า')
#รหัสสินค้า
code = input('ป้อนรหัสสินค้า : ')
#ราคาสืนค้า
price = int(input('ป้อนราคาสินค้า : '))
#ราคาสินค้า
order = int(input('ป้อนจำนวนสินค้า : '))


if code[1] == '1':
    outless = price * order * 0.03
    out = (price*order)-outless
    
    print('ราคาส่วนลด: ',outless)
    print('ราคาที่ต้องจ่าย: ' , out)
elif code[1] == '2' :
    
    if order <= 3:
        outless = price * order * 0.03
        out = (price*order)-outless
        print('ราคาส่วนลด:',outless)
        print('ราคาที่ต้องจ่าย: ' , out)

    elif order > 3:
        outless = price * order * 0.05
        out = (price*order)-outless
        print('ราคาส่วนลด:',outless)
        print('ราคาที่ต้องจ่าย: ' , out)

else :
    out = price*order
    print('สินค้าดังกล่าวไม่ลดราคา')
    print('ราคาที่ต้องจ่าย: ' , out)


'''คำนวนราคาส่วนลดแสดงผล เงื่อนไขคือ ตรวจสอบจากหมวดหมู่สินค้า หมวดหมู่ดูจากก
รหัสสินค้าตำแหน่งที่2 เช่น P1009 (สินค้าหมด1)
หมวด 1 ลด 3%
หมวด 2 น้อยกว่า 3ชิ้น ลด3% แต่ มากกว่า 3 ลด5%
หมวดอื่นไม่ลด
'''