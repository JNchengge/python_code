def f1(a):
    max_num=0
    min_num=100000
    for elem in a:
        if elem>max_num:
            max_num=elem
        if elem<min_num:
            min_num=elem
    return (max_num,min_num,len(a))

def f2(a):
    max_str=""
    min_str="~"
    for elem in a:
        if elem>max_str:
            max_str=elem
        if elem<min_str:
            min_str=elem
    return (max_str,min_str,len(a))

def f3(a):
    max_character=''
    min_character='z'
    for elem in a:
        if elem>min_character:
            max_character=elem
        if elem<min_character:
            min_character=elem
    return (max_character,min_character,len(a))
list1=[9,7,8,3,2,1,55,6]
list2=['apple','pear','melon','kiwi']
list3='TheQuickBrownFox'
tuple1=f1(list1)
tuple2=f2(list2)
tuple3=f3(list3)
print("list=",list1)
print("最大值：",tuple1[0],"最小值：",tuple1[1],"元素个数：",tuple1[2])
print("list=",list2)
print("最大值：",tuple2[0],"最小值：",tuple2[1],"元素个数：",tuple2[2])
print("list=",list3)
print("最大值：",tuple3[0],"最小值：",tuple3[1],"元素个数：",tuple3[2])