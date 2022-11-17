def sumTwoSmallestNums(listo):
    list1 = []
    list2 = []

    result = listo[0]
    i = 0
    for  j in listo:
        if j < result and j > 0:
            result = j
    list1.append(result)
    i+=1

    listo.remove(result)
    
    result = listo[0]
    i = 0
    for  j in listo:
        if j < result and j > 0:
            result = j
    list1.append(result)
    i+=1  

    return sum(list1)

print(sumTwoSmallestNums([10,343445353,3453445,3453545353453,]))
print(sumTwoSmallestNums([19,5,42,2,77]))
print(sumTwoSmallestNums([2,9,6,-1,]))
print(sumTwoSmallestNums([879,953,6944,-847,342,221,-91,-723,791,-587]))
print(sumTwoSmallestNums([3683,2902,3951,-475,1617,-2385]))



