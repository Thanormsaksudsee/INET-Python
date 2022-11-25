h1 = 22
h2 = 25
list1= []
for i in range(h1,h2+1):
    i = str(i)
    i =  ','.join(i)
    i = i.split(',')
    for j in i:
        j = int(j)
        if j % 2 != 0 :
            
            list1.append(j)
list1 = sum(list1)
print(list1)

