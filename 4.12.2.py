def triangles():
    a=[1]
    n=5
    while n:
        yield a
        a=[sum(i) for i in zip([0]+a,a+[0])]
        n-=1
temp=""
for row in triangles():
    for num in row:
        temp+=" "
        temp+=str(num)
    temp+=" "
    print(temp.center(20))
    temp=""

