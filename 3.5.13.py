n=-1
ans_for=1
ans_while=1
while n<0:
    try:
        n=int(input("请输入非负整数n："))
    except ValueError:
        n=int(input("请输入非负整数n："))
m=n
if n==0:
    print("for循环：0!=1")
    print("while循环：0!=1")
else:   
    for i in range(1,n+1):
        ans_for*=i
    while m:
        ans_while*=m
        m-=1
    print("for循环：%d!=%d"%(n,ans_for))
    print("while循环：%d!=%d"%(n,ans_while))