import time
class Student:
    def __init__(self,num,name,birth=(0,0,0)):
        self.num=num
        self.name=name
        self.birth=birth
    def cal_age(self):
        notleap_month=[31,27,31,30,31,30,31,31,30,31,30,31]
        leap_month=[31,28,31,30,31,30,31,31,30,31,30,31]
        now=time.localtime(time.time())
        now_year=now[0]
        now_day=now[7]
        delta_year=now_year-self.birth[0]
        flag=0
        day=0
        if now_year%100!=0 and now_year%4==0:
            flag=1
        elif now_year%100==0 and now_year%400==0:
            flag=1
        if flag:
            for i in range(self.birth[1]):
                day+=leap_month[i]
        else:
            for i in range(self.birth[1]):
                day+=notleap_month[i]
        day+=self.birth[2]
        if day<now_day:
            age=delta_year
        else:
            age=delta_year-1
        return age
    
stu1=Student(123,"xiaoming",(2000,12,7))
stu2=Student(124,"xiaohong",(2000,5,17))
age1=stu1.cal_age()
age2=stu2.cal_age()
print(age1)
print(age2)