import string
class Password:
    def __init__(self,passwd):
        if passwd:
            self.passwd=passwd
            self.score=0
            self.grade=''
        else:
            exit(0)
    def len_score(self):
        a=len(self.passwd)
        if a<=4:
            return 5
        elif a>5 and a<=7:
            return 10
        else:
            return 25
    def char_score(self):
        l=string.ascii_lowercase
        u=string.ascii_uppercase
        ll=0
        uu=0
        for i in self.passwd:
            if i in l:
                ll=1
            elif i in u:
                uu=1
            if ll==1 and uu==1:
                break
        t=ll+uu
        if t==0:
            return 0
        elif t==1:
            return 10
        else:
            return 20
    def num_score(self):
        d=[]
        for i in self.passwd:
            if i>='0' and i<='9':
                d.append(i)
        if len(d)==0:
            return 0
        elif len(d)==1:
            return 10
        else:
            return 20
    def symbol_score(self):
        s=string.punctuation
        count=0
        for i in self.passwd:
            if i in s:
                count+=1
            if count==2:
                break
        if count==0:
            return 0
        elif count==1:
            return 10
        else:
            return 20
    def reward(self):
        if self.char_score()==20 and self.num_score()>0 and self.symbol_score()>0:
            return 5
        elif self.char_score()>0 and self.num_score()>0 and self.symbol_score()>0:
            return 3
        elif self.char_score()>0 and self.num_score()>0:
            return 2
        else:
            return 0
    def cal(self):
        self.score=self.score+self.len_score()+self.char_score()+self.num_score()+self.symbol_score()+self.reward()
        a=self.score
        if a>=90:
            self.grade='Very Secure'
        elif a>=80 and a<90:
            self.grade='Secure'
        elif a>=70 and a<80:
            self.grade='Very Strong'
        elif a>=60 and a<70:
            self.grade='Strong'
        elif a>=50 and a<60:
            self.grade='Average'
        elif a>=25 and a<50:
            self.grade='Weak'
        else:
            self.grade='Very Weak'
a=input("请输入密码：")
p=Password(a)
p.cal()
print("len",p.len_score())
print("char",p.char_score())
print("num",p.num_score())
print("symbol",p.symbol_score())
print("reward",p.reward())
print(p.score)
print(p.grade)
