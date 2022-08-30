def main():
    infile = open('philosophers.txt','r')

    line1 = infile.read()
    line2 = infile.read()
    line3 = infile.read()


    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')


    infile.close()

    print(line1)
    print(line2)
    print(line3)

main()