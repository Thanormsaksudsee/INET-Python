try:
    msg = input("Please enter a message : ")
except:
    msg = ''

upperLetters = 0
lowerLetters = 0

for i in msg:
    if (i.islower()):
        lowerLetters = lowerLetters + 1
    elif (i.isupper()):
        upperLetters = upperLetters + 1

print("All capital letters : "+str(upperLetters) )
print("All lowercase letters : "+str(lowerLetters) )