import sys
n=int(sys.argv[1])
power=1
a=0
i=0
f=open('out.log','w')
sys.stdout=f
while i<=n:
    print("%d\t%d\t%d\t"%(i,a,power))
    i+=1
    a=i*2
    power=power*2
sys.stdout=sys.__stdout__
f.close()