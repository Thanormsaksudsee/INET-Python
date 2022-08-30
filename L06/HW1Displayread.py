def BigKuma():
    displayFile = open('Display.txt', 'r')
    line = displayFile.readline()
    name = []
    ID = []
    Dept = []
    
    reck = 1
    while line != '':
        line = line.strip('\n')
        
        if reck % 3 == 1:
            name.append(line)
        if reck % 3 == 2:
            ID.append(line)
        if reck % 3 == 0:
            Dept.append(line)
            
        reck += 1
        line = displayFile.readline()
            
    displayFile.close()
    for i,j,k in zip(name,ID,Dept):
        print("Name:", i)
        print("ID:",  j)
        print("Dept:", k)
            
BigKuma()