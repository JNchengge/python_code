def equation_way(h,f):
    r=(f/2)-h
    c=h-r
    if r>0 and c>0:
        print("方法一：鸡：%d只，兔：%d只"%(c,r))
    else:
        print("无解，请重新运行测试！")
def enum_way(h,f):
    c=0
    r=h
    while r>=0:
        if c*2+r*4==f:
            break
        else:
            c+=1
            r-=1
    if r<0:
        print("无解，请重新运行测试！")
    else:
        print("方法二：鸡：%d只，兔：%d只"%(c,r))
h=int(input("请输入总头数："))
f=int(input("请输入总脚数（必须是偶数）："))
while f%2!=0:
    f=int(input("请输入总脚数（必须是偶数：）"))
equation_way(h,f)
enum_way(h,f)
    