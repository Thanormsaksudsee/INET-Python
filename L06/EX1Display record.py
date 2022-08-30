def main():
    
    
    empFile = open('Display.txt', 'r')
    line = empFile.read()



    while line != '':
        
        print(line)

        line = empFile.read()

    empFile.close()



main()

