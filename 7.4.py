import time,sys
import getpass
class NotInUserList(Exception):
    def __init__(self,data):
        Exception.__init__(self,data)
        self.data=data
    def __str__(self):
        return ('[error] '+self.data+' is not exist '+time.asctime(time.localtime(time.time())))

class PasswordError(Exception):
    def __init__(self,data):
        Exception.__init__(self,data)
        self.data=data
    def __str__(self):
        return "[warning] "+self.data+" Password error three times "+time.asctime(time.localtime(time.time()))

user_list=[]
locked_list=[]
dic={}

f=open('user_list.txt','r')
for line in f:
    user_list.append(line.strip().split(' '))
f.close()

f=open('warnlog,txt','a+')
f2=open('locked.txt','r')
for i in user_list:
    dic[i[0]]=i[1]
for line in f2:
    locked_list.append(line.strip())

username=input("请输入用户名：")
password=getpass.getpass("请输入密码：")

if dic.__contains__(username)!=True:
    f.write('[error] '+username+' is not exist '+time.asctime(time.localtime(time.time()))+'\n')
    raise NotInUserList(username)
elif username in locked_list:
    print("用户已锁定！")
elif username not in locked_list:
    flag=0
    for i in range(3):
        if password!=dic[username]:
            if flag!=3:
                print('密码错误，请重新输入，剩余机会'+str(3-flag)+'次')
            flag+=1
            password=getpass.getpass("请输入密码：")
    if flag==3:
        print('密码错误已三次，锁定用户！')
        locked_list.append(username)
        f2=open('locked.txt','a+')
        f2.write(username+'\n')
        f.write("[warning] "+username+" Password error three times "+time.asctime(time.localtime(time.time()))+'\n')
        raise PasswordError(username)
if dic.__contains__(username)==True and dic[username]==password:
    print('登陆成功！')
f.close()
f2.close()

