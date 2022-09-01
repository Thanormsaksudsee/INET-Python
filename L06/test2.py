import re
fr = open("Display.txt",'r')
name = input('Enter name your want to find : ')

for mem in fr:
    see = re.search(name,mem)
    keep = fr.readline()
    if  see != None :
        print('Name:',mem.strip())
        print('ID:',keep.strip())
        keep = fr.readline()
        print('dept:',keep.strip())
        keep = fr.readline()


fr.close()