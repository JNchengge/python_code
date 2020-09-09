def selectSort(a):
    for i in range(0,len(a)):
        m=i
        for j in range(i+1,len(a)):
            if a[j]<a[m]:
                m=j
        a[i],a[m]=a[m],a[i]
