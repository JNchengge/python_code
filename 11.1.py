import stack
s=stack.Stack(100)#设置长度为100的栈
crackets=input()
flag=True
for cracket in crackets:
    if cracket=='(':
        s.push(cracket)
    else:
        if not s.empty():
            s.pop()
        else:
            flag=False
if not s.empty():
    flag=False
print(flag)
