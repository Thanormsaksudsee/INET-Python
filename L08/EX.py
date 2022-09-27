# 1 แสดงข้อมูล display reccord 
# 2search ID 
# 3Add 
# 4modifide reccord แก้ไข 
# 5del reccord 
# 6exist record
records = {'650602260095':['Anirach Mingkhwan','Anirach@gmail.com','0817320766']}

print(records)

#1Display
def Display():
    print(records)
def Search():
    search = input('Please Search : ')
    print(records.keys(),records.get(search))
def Add():
    Display()
    addKey = input('Add Enter ID: ')
    addName = input('Add Enter Name: ')
    addMail = input('Add Enter Email: ')
    addPhone = input('Add Enter Phone Number: ')
    records[addKey] = addName , addMail , addPhone
    print(records)
def Modifier():
    Display()
    addKey = input('Modifier Enter ID: ')
    addName = input('Modifier Enter Name: ')
    addMail = input('Modifier Enter Email: ')
    addPhone = input('Modifier Enter Phone Number: ')
    records[addKey] = addName , addMail , addPhone
    print(records)
def Del():
    addKey = input('Delete Enter ID: ')
    records.pop(addKey)
    print(records)
def Exits():
    name = input('Exits ID : ')     
    if(name in records ):
        print(name , 'found index = ',len(name))
        Display()
    if(name not in records):
        print(name , 'not found')
        Display()    

def main():
    keep = 'y'
    while keep == 'y':
        print('1.Display Records Function')
        print('2.Search Records Function')
        print('3.Add Records Function')
        print('4.Modifier Records Function')
        print('5.Delete Records Function')
        print('6.Exist Funtion')
        Select = int(input('Please Seclect Funtion : '))
        
        if Select == 1:
            Display()
        elif Select == 2:
            Search()
        elif Select == 3:
            Add()
        elif Select == 4:
            Modifier()
        elif Select == 5:
            Del()
        elif Select == 6:
            Exits()
        else:
            print('อย่าเปรี้ยวไอสัสพิมพ์ดีๆ')
            
        keep = input('Enter y for Moretime Enter n for Exit: ')
main()