World1 = input('Input Sting: ')

def Letters():
    World2 = World1.split()
    total = (len(World1)) - (len(World2)) +1
    print('Number of Letters: ',total)
Letters()

def vowels():
    count = 0
    for i in World1:
        if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o'or i == 'O'or i == 'u'or i == 'U':
            count +=1
    print('Number of vowels: ',count)
vowels()


def Capital():
    count = 0
    list = []
    for i in World1:
        if (i.isupper()):
            count +=1
            list.append(i)
    print('Number of Capital: ',count,'[%s]' % ','.join(map(str,list)))
    
Capital()
