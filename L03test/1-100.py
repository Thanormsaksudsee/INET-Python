rows = int(input('Enter Colum'))


for i in range(1,101):
    print(i,end=' ')
    if i % rows == 0:
        print()