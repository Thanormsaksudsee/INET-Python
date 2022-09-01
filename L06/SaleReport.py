'''total = 0.0

try: 
    
    infile = open('friends.txt', 'friends.txt'
    , 'r')
    
    
    for line in infile:
        amount = float(line)
        total += amount

        infile.close()

        print(format(total, ',.2f'))

except IOError:
    print('An error occurred trying to read')
except ValueError:
    print('ERROR: Hours worked and hourly pay rate must')
except:
    print('An error occured.')'''


total = 0.0

try: 
    
    infile = open('sales.txt','r')
    
    
    for line in infile:
        amount = float(line)
        total += amount

    infile.close()
except Exception as err:
    print(err)
else:
    print(format(total, ',.2f'))