acc10=['Charlie',['credit',0.0]]
acc11=acc10
print(id(acc10))
print(id(acc11))
print(acc10 is acc11)
a=acc10[1]
b=acc10[1].copy()
print(a is b)
c=acc10.copy()
print(a is c[1])