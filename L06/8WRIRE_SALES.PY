def main():
    numDays = int(input('For many day do ' + \
                        'you have sales? '))
    saleFile = open('sales.txt', 'w')


    for count in range(1, numDays + 1):
        sales = float(input('Enter the sales for day #' +
                            str(count) + ': '))
    
        saleFile.write(str(sales) + '\n')
    saleFile.close()
    print('Data written  to sales.txt.')

main()

