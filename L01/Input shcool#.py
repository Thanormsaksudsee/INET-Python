first_name = input('Enter your first name: ')
last_name = input('Enter your last name:')
print('Hello' , first_name, last_name)

###############################

name = input('What is you name?')
age = int(input('What is your age?'))
income = float(input('What is you income?'))

print('Here is the data you entered:')
print('Name:',name)
print('Age:', age)
print('Income: ', format(income, ' 12,.2f'))

##############################

a,b,c = input().split()
print('a =',a)
print('b =',b)
print('c =',c)

############################



a,b,c = [int(e) for e in input().split()]
print('a = ',a)
print('b = ',b)
print('c = ',c)

#############################

a,b,c = [float(e) for e in input().split()]
print('a =',a)
print('b =',b)
print('c =',c)

###########################