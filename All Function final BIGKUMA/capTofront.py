def capTofront(word):
    list1 = []
    list2 = []
    for i in word:
        if i == i.upper():
            list1.append(i)
        if i == i.lower():
            list2.append(i)
        result = ''.join(list1+list2)             
    return result
print(capTofront("hApPy"))
print(capTofront("moveMENT"))
print(capTofront("shOrtCAKE"))