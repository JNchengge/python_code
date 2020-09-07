list1=[1,2,3]
list2=[3,4,5]
dict1={'1':list1,'2':list2}
dict2=dict1.copy()
dict1['1'][0]=15
print(dict1['1'][0]+dict2['1'][0])  