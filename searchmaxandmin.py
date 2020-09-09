def max1(alist):
    pos=0
    iMax=alist[0]
    while pos<len(alist):
        if alist[pos]>iMax:
            iMax=alist[pos]
        else:
            pos+=1

def min1(alist):
    pos=0
    iMin=alist[0]
    while pos<len(alist):
        if alist[pos]<iMin:
            iMin=alist[pos]
        else:
            pos+=1
