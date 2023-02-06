def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    count = 1
    while first<=last and not found:
        count = count+1
        midpoint = (first + last )//2 
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    
    
    return found,count-1
    
testlist = [17,20,26,31,44,54,55,65,77,93]
print(binarySearch(testlist, 55))
