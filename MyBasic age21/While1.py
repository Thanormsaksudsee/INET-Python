import random

print("What is my magic number (1 to 100) ?")
mynumber = random.randint (1, 5)
ntries   = 1
yourguess= -1
while ntries < 7  and  mynumber != yourguess :   
    msg = str(ntries) + ">>"
    if (ntries == 6) :
        print("ครั้งสุดท้ายแล้วนะ")
    yourguess = int(input(msg))
    if yourguess > mynumber :
        print("--> too high")
    elif yourguess < mynumber :
        print("--> too low")
    ntries += 1
    
if  yourguess == mynumber :
    print("Yes! it's" , mynumber)
else :
    print("Sorry! my number is", mynumber)