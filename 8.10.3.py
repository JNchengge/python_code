def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
a=[]
a=list(map(fib,range(1,21)))
for i in range(0,20):
    print(str(a[i]).rjust(5),end=" ")
    if i==9:
        print("\n")
print("\n")