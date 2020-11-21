# 循环法
f=[0,1,1]
for i in range(18):
    f.append(f[-1]+f[-2])
for i in range(1,21):
    print(str(f[i]).rjust(5),end=" ")
    if i==10:
        print("\n")
print("\n")