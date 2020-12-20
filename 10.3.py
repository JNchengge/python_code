from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.text import MIMEText
import smtplib

from_addr="13415616998@163.com"
to_addr="13415616998@163.com"
passwd="UPJWDVQAJWHOYSQG"
#创建文本邮件
context="python程序设计"
mime=MIMEText(context,_subtype='plain',_charset='utf-8')
mime["Subject"]=Header('Test','utf-8').encode()
#构造收发人信息
name,addr=parseaddr("chenghao<%s>"%from_addr)
mime["From"]=formataddr((Header(name,'utf-8').encode(),addr))
name,addr=parseaddr("chenghao<%s>"%to_addr)
mime["To"]=formataddr((Header(name,'utf-8').encode(),addr))

server='smtp.163.com'
smtp=smtplib.SMTP(server,25)
smtp.login(from_addr,passwd)
smtp.sendmail(from_addr,[to_addr],mime.as_string())
smtp.quit()