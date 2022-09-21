def main()
    
    def Display():
        heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
        print(print)
    Display()

    def add():
    
        heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
        heroes.append('BIGKUMA')
        print(heroes)

    add()



    def Remove():
        heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
        heroes.remove('Ironman')
        print(heroes)
    Remove()

    def DisSort():
        heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
        heroes.sort()
        print(heroes)
    DisSort()

    def Exis():
        name = input('Hero name')     
        heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
        if(name in heroes ):
            print(name , 'found')
        if(name not in heroes):
            print(name , 'not found')
    Exis()
        
        
main()