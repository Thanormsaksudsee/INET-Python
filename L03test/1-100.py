colum = int(input('Enter Colum'))


for i in range(1,101):
    print(i,end=' ')
    for j in range(1,100,colum):
        if i == j:
            
            print('\n')
        