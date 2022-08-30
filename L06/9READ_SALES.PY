def main():
    saleFile = open('sales.txt', 'r')


    line = saleFile.readline()
    while line != '':
        amount = float(line)

        print(format(amount, '.2f'))
        line = saleFile.readline()

    saleFile.close()

main()
