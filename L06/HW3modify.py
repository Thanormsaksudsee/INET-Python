import os
fhR = open("Display.txt",'r')
fhW = open('temp.txt','w')

name = input('Enter name : ')

s=' '
while(s):
    s=fhR.readline()
    l=s.split('\n')
    if len(s)>0:
        if (l[0])==name:
            name=input('Enter name : ')
            ID=input('Enter ID : ')
            dept=input('Enter Dept : ')
            fhW.write(name+'\n'+ID+'\n'+dept+'\n')
        else:
            fhW.write(s)
fhW.close()
fhR.close()
os.remove('Display.txt')
os.rename('temp.txt','Display.txt')


