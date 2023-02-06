def binarySearch(alist, item):

    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)
    


testlist = [17,20,26,31,44,54,55,65,77,93]
print(binarySearch(testlist, 55))



