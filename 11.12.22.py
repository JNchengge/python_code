import random
a=[]
b=[]
for n in range(1,6):
    a.append(random.randint(0,10))
    b.append(random.randint(0,10))
c=set(a)
d=set(b)
print("集合的内容、长度、最大值、最小值分别为：")
print(c,str(len(c)),str(max(c)),str(min(c)))
print(d,str(len(d)),str(max(d)),str(min(d)))
print("A和B的并集、交集和差集分别为：")
print(c|d,c&d,c-d)