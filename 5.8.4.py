s=[9,7,8,3,2,1,55,6]
max_num=s[0]
min_num=s[0]
sumary=0
for num in s:
    max_num,min_num=max(max_num,num),min(min_num,num)
    sumary+=num
average=sumary/len(s)
print("最大值：%d，最小值：%d，元素和：%d，平均值：%.2f"%(max_num,min_num,sumary,average))
