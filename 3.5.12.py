a=float(input("请输入系数a:"))
b=float(input("请输入系数b:"))
c=float(input("请输入系数c:"))
delta=b**2-4*a*c
if a==0 and b==0:
    print("此方程无解！")
elif a==0 and b!=0:
    x=(-1)*(b/c)
    print("此方程的解为：%.1f"%x)
elif delta==0:
    x=(-1)*(b/(2*a))
    print("此方程有两个相等实根：%.1f"%x)
elif delta>0:
    x1=(-1)*(b/(2*a))+delta**0.5/(2*a)
    x2=(-1)*(b/(2*a))-delta**0.5/(2*a)
    print("此方程有两个不等实根：%.1f 和 %.1f"%(x1,x2))
elif delta<0:
    realPart=(-1)*(b/(2*a))
    imagPart=(-delta)**0.5/(2*a)
    print("此方程有两个共轭复根：%.1f + %.1fi 和 %.1f - %.1fi"%(realPart,imagPart,realPart,imagPart))

