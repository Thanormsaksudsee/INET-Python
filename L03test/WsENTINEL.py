keep_going = 'y'

while keep_going == 'y':
    sales = float(input("Enter the item's wholesale cost: "))
    Retailpricen = sales*2.5
    print('Retail price $' , format(Retailpricen, ',.2f'))
    keep_going = input('Do you have another item? (Enrer y for yes):')