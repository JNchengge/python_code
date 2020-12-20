#VerificationCode.py
import string
import random
def gen():   
    v=''
    s=string.ascii_letters+string.digits
    ch=[]
    for i in s:
        ch.append(i)
    for i in range(6):
        index=random.randint(0,len(ch)-1)
        v+=ch[index]
    return v