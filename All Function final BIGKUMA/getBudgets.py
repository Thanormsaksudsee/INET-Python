def getBudgets(big):
    big1 = big[0]['budget']
    big2 = big[1]['budget']
    big3 = big[2]['budget']
    result = big1+big2+big3
    return result

print(getBudgets([
{'name': "Jonh", 'age': 21, 'budget': 23000},
{'name': "Steve", 'age': 32, 'budget': 40000},
{'name': "Martin", 'age': 16, 'budget': 2700}]))

print(getBudgets([
{'name': "Jonh", 'age': 21, 'budget': 29000},
{'name': "Steve", 'age': 32, 'budget': 32000},
{'name': "Martin", 'age': 16, 'budget': 1600}]))


