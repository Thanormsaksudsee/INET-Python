heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
def Exits():
    name = input('Exits Heroes : ')     
    if(name in heroes ):
        print(name , 'found index = ',len(name))
        print(heroes)
    if(name not in heroes):
        print(name , 'not found')
        print(heroes)    
