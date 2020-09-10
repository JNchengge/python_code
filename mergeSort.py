import argparse
def merge(a,b):
    c=[]
    m,n=0,0
    while m<len(a) and n<len(b):
        if a[m]<=b[n]:
            c.append(a[m])
            m+=1
        else:
            c.append(b[n])
            n+=1
    c.extend(a[m:]) #extend方法，一次性添加剩余的值
    c.extend(b[n:])
    return c

def mergeSort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=mergeSort(a[:mid])
    right=mergeSort(a[mid:])
    return merge(left,right)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--list',type=str)
    args=parser.parse_args()
    a=[]
    for num in args.list.split(','):
        a.append(int(num))
    print(mergeSort(a))