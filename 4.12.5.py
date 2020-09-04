salary=float(input("请输入有固定收入的党员的月工资："))
if salary<=3000:
    f=0.5*0.01*salary
elif salary>3000 and salary<=5000:
    f=1.0*0.01*salary
elif salary>5000 and salary<=10000:
    f=1.5*0.01*salary
elif salary>10000:
    f=2.0*0.01*salary
print("月工资：%.0f，缴纳党费：%.1f"%(salary,f))
