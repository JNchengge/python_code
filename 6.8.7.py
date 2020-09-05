import getpass
username=input("用户名：")
password=getpass.getpass("密码：")
if username=="jianghong" and password=="password":
    print("登录成功")
else:
    print("登陆失败")