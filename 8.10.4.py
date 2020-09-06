def min_n(a,b,*c):
    if a<b:
        ans=a
    else:
        ans=b
    for num in c:
        if num<ans:
            ans=num
    return str(ans)
print(min_n(8,2))
print(min_n(16,1,7,4,15))