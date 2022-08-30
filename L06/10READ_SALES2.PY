def main():
    saleFile = open('sales.txt', 'r')

    for line in saleFile:
        amount = float(line)

        print(format(amount, '.2f'))

    saleFile.close

main()




