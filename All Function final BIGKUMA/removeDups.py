def removeDups(Butter):
    list1 = []
    for i in range(len(Butter)):
        if Butter[i] not in list1:
            list1.append(Butter[i])

    return list1


print(removeDups(["John", 'Taylor', 'John']))
print(removeDups([1,0,1,0]))
print(removeDups(["The", 'big', 'cat']))






