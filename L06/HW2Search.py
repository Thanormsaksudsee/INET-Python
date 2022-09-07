emp = open('Display.txt','r')
name = input('Enter name')
line = emp.readline()
while line != '':
    if line.strip() == name:
        print('name: ',line.strip())
        line = emp.readline()
        print('ID:',line.strip())
        line = emp.readline()
        print('dept:',line.strip())
        line = emp.readline()
    line = emp.readline()
emp.close()