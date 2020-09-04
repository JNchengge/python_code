peaches=[1]
day=7
while day:
    peaches.append((peaches[-1]+1)*2)
    day-=1
n=8
for peach in peaches:
    print("第%d天桃子数为：%d"%(n,peach))
    n-=1


