str1=input("请输入一个字符串")
str1_reverse=str1[::-1]
if str1==str1_reverse:
    print("是回文字符串")
else:
    print("不是回文字符串")