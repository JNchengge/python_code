salary=float(input("请输入有固定收入的党员的月工资："))
if salary<=400:
    f=0.5*0.01*salary
elif salary>401 and salary<=600:
    f=1.0*0.01*salary
elif salary>601 and salary<=800:
    f=1.5*0.01*salary
elif salary>800 and salary<=1500:
    f=2.0*0.01*salary
elif salary>1500:
    f=3.0*0.01*salary
print("月工资：%.0f，缴纳党费：%.1f"%(salary,f))
