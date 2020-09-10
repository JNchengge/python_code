import argparse
def selectSort(a):
    for i in range(0,len(a)):
        m=i
        for j in range(i+1,len(a)):
            if a[j]<a[m]:
                m=j
        a[i],a[m]=a[m],a[i]

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--list',type=str)
    args=parser.parse_args()
    a=[]
    for num in args.list.split(','):
        a.append(int(num))
    selectSort(a)
    print(a)