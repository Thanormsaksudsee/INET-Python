heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spiderman']
def Insert():
    print(heroes)
    Hero = input('Add Heroes : ')
    index = int(input('Insert Heroes :'))
    heroes.insert(index,Hero)
    print(heroes)
