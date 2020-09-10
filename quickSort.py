import argparse
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

parser=argparse.ArgumentParser()
parser.add_argument('--list',type=str)
args=parser.parse_args()
a=[]
for num in args.list.split(','):
    a.append(int(num))
quickSort(a,0,len(a)-1)
print(a)