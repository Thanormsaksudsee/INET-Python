emp = open('Display.txt','r')

line = emp.readline()
while line != '':
    print('name: ',line.strip('\n'))
    line = emp.readline()
    print('ID:',line.strip('\n'))
    line = emp.readline()
    print('dept:',line.strip('\n'))
    line = emp.readline()
emp.close()