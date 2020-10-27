characters=[]
spans=[]
numbers=[]
others=[]
s=input("请输入一行字符：")
for i in s:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        characters.append(i)
    elif (i>='0' and i<='9'):
        numbers.append(i)
    elif (i==' '):
        spans.append(i)
    else:
        others.append(i)
print("英文字母个数为：",len(characters))
print("空格个数为：",len(spans))
print("数字个数为：",len(numbers))
print("其他字符个数为：",len(others))

