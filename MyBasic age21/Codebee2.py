going = "y"
while going == 'y':

    print("please select operation - ")
    print(" 1 = add + \n 2 = subtract- \n 3 = multiply * \n 4 = divide /")
    select = int(input("select number to calculate: " ))
    if select >= 5 or select == 0 :
        going = 'n'
        print("WTF")
        break
    num1 = int(input("Enter your number : "))
    num2 = int(input("Enter your number : "))
    
    if select == 1:     
        print(" %d + %d = %d " % (num1 ,num2, num1 + num2))
    elif select == 2:
        print(" %d - %d = %d " %(num1 , num2 ,num1 - num2))
    elif select == 3:
        print(" %d x %d = %d " %(num1 ,num2,num1 * num2))
    elif select == 4:
        print(" %d / %d = %d " %(num1,num2,num1 / num2))
    
    going = str(input("Enter(y) : "))