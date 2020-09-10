import argparse
def bubblesort(a):
    for i in range(len(a)-1,-1,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

parser=argparse.ArgumentParser()
parser.add_argument('--list',type=str)
args=parser.parse_args()
a=[]
for num in args.list.split(','):
    a.append(int(num))
bubblesort(a)
print(a)