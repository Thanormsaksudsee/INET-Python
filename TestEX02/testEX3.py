inChar = input ("Input one character:")
if inChar >= 'A' and inChar <= 'Z' :
    print('You in Upper Case Letter ' ,inChar)
elif inChar >= 'a' and inChar <= 'z' :
    print("You in put Lower Case Letter " , inChar)
elif inChar >= '0' and inChar <='9' :
    print('You input Number '  , inChar)
else :
    print("It's not a letter or number." , inChar)
    