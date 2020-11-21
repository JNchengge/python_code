def d2b(a):
    b=[]
    while a!=0:
        b.append(str(a%2))
        a=a//2
    return '0b'+''.join(b[::-1])

a=123
print(bin(a))
print(d2b(a))