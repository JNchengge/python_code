with open('file1.txt','r') as f1:
    content=f1.readlines()
with open('file2.txt','w') as f2:
    for i in content:
        f2.write(i[::-1])
print('Done!')