def numberSplit(num):
    num1 = num//2
    num2 = num-num1
    
    return [num1,num2]


print(numberSplit(4))
print(numberSplit(10))
print(numberSplit(11))
print(numberSplit(-9))