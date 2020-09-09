def quickSort(a,low,high):
    i=low
    j=high
    if i>=j:
        return a
    key=a[i]
    while i<j:
        while i<j and a[j]>=key:
            j-=1
        a[i]=a[j]
        while i<j and a[i]<=key:
            i+=1
        a[j]=a[i]
    a[i]=key
    quickSort(a,low,i-1)
    quickSort(a,j+1,high)

if __name__=='__main__':
    a=[156,516,5,51,7651,378,413548,1566,573]
    quickSort(a,0,8)
    print(a)
    b=[156,516,5,51,7651,378,413548,1566,573]
    b.sort()
    print(b)
    c=[156,516,5,51,7651,378,413548,1566,573]
    c.sort(reverse=True)
    print(c)