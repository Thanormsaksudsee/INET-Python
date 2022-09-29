World1 = input('Input Sting: ')
def Letters():
    World2 = World1.split()
    total = (len(World1)) - (len(World2)) +1
    print('Number of Letters: ',total)


def vowels():
    count = 0
    for i in range (World1):
        if World1 == 'a' or World1 == 'e' or World1 == 'i' or World1 == 'o' or World1 == 'u':
            count += 1
    print(count)
vowels()

def Capital():
    lit = 0
    for f in World1:
        if (World1.isupper()): 
            lit1 = lit+1
    print(lit1)


