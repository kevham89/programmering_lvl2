def mylist(mylist):
    newlist = []
    for element in mylist:
        newelement = pow(element,2)
        newlist.append(newelement)
    return newlist

print(mylist([2,4,5,6,7,10]))