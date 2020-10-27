n=int(input('n='))
s1=input()
s2=s1.split(' ')
ans=0
for i in range(1,n+1):
    if i%int(s2[0])!=0 and i%int(s2[1])!=0 and i%int(s2[2])!=0:
        ans+=1
print(ans)