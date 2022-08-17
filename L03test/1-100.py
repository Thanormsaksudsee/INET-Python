colum = int(input('Enter Colum'))


for i in range(1,1001):
    print(i,end=' ')
    for j in range(0,1000,colum):
        if i == j:
            print('\n')
    