import random
a=random.randint(0,100)
b=random.randint(0,100)
m=a
n=b
if m>n:
    r=m-int(m/n)*n
    while r:
        m=n
        n=r
        r=m-int(m/n)*n
    m=n
    common_diviser=m
elif m<n:
    r=n-int(n/m)*m
    while r:
        n=m
        m=r
        r=n-int(n/m)*m
    n=m
    common_diviser=n
elif m==n:
    common_diviser=m
common_multiple=(a*b)/common_diviser
print("整数1：%d，整数2：%d"%(a,b))
print("最大公约数=%d，最小公倍数=%d"%(common_diviser,common_multiple))
