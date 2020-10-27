def delete_repeat_elem(list_a):
    b=[]
    b.append(a[0])
    flag=True
    for elem_a in a:
        if elem_a in b:
            flag=False
        if flag:
            b.append(elem_a)
        flag=True
    return b
a=[1,1,2,2,3,4,5,9,1,2]
b=delete_repeat_elem(a)
print(b)
print(set(a))