DISCOUNT_PERCENTAGE = 0.20
def main() :  
    regPrice = getRegularPrice()
    salePrice = regPrice - discount(regPrice)
    print('The sale price is $', format(salePrice, ',.2f'), sep='')

def getRegularPrice():
    price = float(input("Enter the item's regular price: "))
    return price

def discount(price):
    return price * DISCOUNT_PERCENTAGE

main()