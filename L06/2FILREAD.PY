def main():

    infile = open('philosophers.txt', 'r')

    fileContents = infile.read()

    infile.close()

    print(fileContents)

main()