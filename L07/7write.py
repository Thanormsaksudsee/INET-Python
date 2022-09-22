def Kuma():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    outfile = open('/Users/BIGKUMA/INET-Python-2/L07/cities.tx','w')
    
    
    cities = map(lambda x: x+'\n', cities)
    outfile.writelines(cities)
    
    outfile.close()
    





def Kuma():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    outfile = open('/Users/BIGKUMA/INET-Python-2/L07/cities.tx','w')
    
    
    for item in cities:
        outfile.writelines(item)
    
    outfile.close()
    
Kuma()


