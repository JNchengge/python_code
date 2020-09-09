def insertSort(a):
    for i in range(1,len(a)):
        j=i
        while (j>0) and (a[j]<a[j-1]):
            a[j],a[j-1]=a[j-1],a[j]
            j-=1

def myinsertSort(a):
    for i in range(1,len(a)):
        for j in range(i,-1,-1):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]

if __name__=='__main__':
    a=[2,456,151,481546,5135]
    insertSort(a)
    print(a)
    b=[2,456,151,481546,5135]
    myinsertSort(b)
    print(b)


