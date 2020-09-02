basic=int(input("请输入本金："))
rate=float(input("请输入年利率："))*0.01
years=int(input("请输入年数："))
sum=basic
while years:
    sum+=sum*rate
    years-=1
print(str.format("本金利率和为：{0:2.2f}",sum))
