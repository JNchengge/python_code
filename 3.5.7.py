import math
n=1
number=int(input("请输入项数："))
odds=[]
sum=0
while n<=number:
    odd=pow(-1,n-1)*(2*n-1)
    odds.append(odd)
    n+=1
for odd in odds:
    sum+=odd
print(odds)
print(str(sum))