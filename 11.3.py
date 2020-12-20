class Heterotopic:
    def __init__(self,s,t):
        self.s=list(s)
        self.t=list(t)
    def quickSort(self,a,low,high):
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
        self.quickSort(a,low,i-1)
        self.quickSort(a,j+1,high)
    def bubblesort(self,a):
        for i in range(len(a)-1,-1,-1):
            for j in range(i):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
    def method1(self):
        self.quickSort(self.s,0,len(self.s)-1)
        self.quickSort(self.t,0,len(self.t)-1)
        return self.s==self.t
    def method2(self):
        self.bubblesort(self.s)
        self.bubblesort(self.t)
        return self.s==self.t
h=Heterotopic("rat","car")
print(h.method1())
print(h.method2())
