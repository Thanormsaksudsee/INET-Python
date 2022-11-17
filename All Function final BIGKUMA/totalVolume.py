
def totalVolume(big):
    listem = []
    coun = 0
    while coun < len(big):
        total = 1
        for i in big[coun]:
            total = total*i
        listem.append(total)
        coun += 1
        
        result = sum(listem)
    return result

list1 = [4,2,4],[3,3,3],[1,1,2],[2,1,1]
list2 = [4,2,4],[3,3,3]
print(totalVolume(list1))
print(totalVolume(list2))






































