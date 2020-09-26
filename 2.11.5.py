import math
a=1
b=10
c=16
d=b**2-4*a*c
x1=(-float(b)+math.sqrt(d))/2
x2=(-float(b)-math.sqrt(d))/2
print("方程x*x+10*x+16=0的解为： %.1f %.1f"%(x1,x2))