import copy
#!/usr/bin/
deeper=[4,5,6]
origin=[1,2,3,deeper]
_copy=origin.copy()
z=origin
x=[1,2,3,deeper]
print(id(deeper))
print(id(origin))
print(id(_copy))
print(deeper is [3])
print(z is origin)
print(x is origin)
print(x[3] is deeper)
_copy=copy.deepcopy(origin)