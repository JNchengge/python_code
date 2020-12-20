class Binarysearch:
    def __init__(self,l,target):
        self.l=l
        self.target=target
    def binarysearch(self,key,alist,low,high):
        while low<=high:
            mid=(low+high)//2
            if alist[mid]>key:
                high=mid-1
            elif alist[mid]<key:
                low=mid+1
            else:
                return mid
        return -1
    def way1(self):
        low=0                #取最低值
        high=len(self.l)-1    #取最高值
        while low<high:
            now=self.l[low]+self.l[high]
            if now==self.target:
                print(low+1,high+1)
                break
            elif now>self.target:
                high=high-1
            elif now<self.target:
                low=low+1
        if low==high:
            print("找不到符合条件的数！")
    def way2(self):
        low=0                #取最低值
        high=len(self.l)-1    #取最高值
        for i in range(len(self.l)-1,-1,-1):
            key=self.target-self.l[i]
            high=i
            j=self.binarysearch(key,self.l,low,high)
            if j+1:
                print(j+1,i+1)
                break
        if not j+1:
            print("找不到符合条件的数！")
b=Binarysearch([2, 7, 11, 15],9)
b.way1()
b.way2()