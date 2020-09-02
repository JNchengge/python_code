import math
def getValue(b,r,n):
    v=float(b*pow(1+r,n))
    return v
b=float(input("请输入本金："))
r=float(input("请输入年利率："))*0.01
n=int(input("请输入年数："))
amount=getValue(b,r,n)
print("总金额为：%.2f"%amount)