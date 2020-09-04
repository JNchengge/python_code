n=9
total=0
height=100.0
while n:
    height*=1/2
    total=total+2*height
    n-=1
print("小球在第10次落地时，共经过%.2f米"%total)
print("第10次反弹%.2f米"%(height))