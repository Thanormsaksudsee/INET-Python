def Kuma():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    outfile = open('/Users/thano/INET-Python/L07/cities.tx','w')
    
    
    cities = map(lambda x: x+'\n', cities)
    outfile.writelines(cities)
    
    outfile.close()
    
Kuma()