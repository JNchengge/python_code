import random
a=random.randint(0,100)
b=random.randint(0,100)
m,n=max(a,b),min(a,b)
r=m-int(m/n)*n
while r:
    m=n
    n=r
    r=m-int(m/n)*n
m=n
common_diviser=m
if m==n:
    common_diviser=m
common_multiple=(a*b)/common_diviser
print("整数1：%d，整数2：%d"%(a,b))
print("最大公约数=%d，最小公倍数=%d"%(common_diviser,common_multiple))
