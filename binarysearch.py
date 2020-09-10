import argparse
def _binarysearch(key,alist,low,high):
    if high<=low:
        return -1
    mid=(low+high)//2
    if alist[mid]>key:
        return _binarysearch(key,alist,low,mid)
    elif alist[mid]<key:
        return _binarysearch(key,alist,mid+1,high)
    elif alist[mid]==key:
        return mid

def binarysearch(key,alist):
    return _binarysearch(key,alist,0,len(alist))

def binarysearch_not_recursion(key,alist):
    low=0
    high=len(alist)-1
    while low<=high:
        mid=(low+high)//2
        if alist[mid]>key:
            high=mid-1
        elif alist[mid]<key:
            low=mid+1
        else:
            return mid
    return -1

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--list',type=str)
    parser.add_argument('--key')
    args=parser.parse_args()
    a=args.list.split(',')
    b=[]
    key=int(args.key)
    for num in a:
        b.append(int(num))
    if binarysearch_not_recursion(key,b)>=0:
        print("found")
    else:
        print("not found")