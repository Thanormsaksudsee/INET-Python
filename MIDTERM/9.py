inputmsh = input('Enter your world: ')
pig = inputmsh.split()

for i in range (len(pig)) :             
    if pig[i][0] == 'A' or pig[i][0] == 'E' or pig[i][0] == 'I' or pig[i][0] == 'O' or pig[i][0] == 'U':
        pig[i]   =  pig[i] + 'HAY'
            
    else :
        pig[i]  =  pig[i][1:] + pig[i][0] + 'AY'

    
    print(pig[i]+' ',end='')