for i in range(1,10):
    for j in range(1,10):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print()

print("——————————————————————————————————————————————————————————————")

for i in range(1,10):
    for j in range(i,10):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print()

print("——————————————————————————————————————————————————————————————")

for i in range(1,10):
    for j in range(1,i+1):
         print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print()       

print("——————————————————————————————————————————————————————————————")

for i in range(1,10):
    for k in range(1,i):
        print(end="       ")
    for j in range(i,10):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print()

print("——————————————————————————————————————————————————————————————")

for i in range(1,10):
    for k in range(1,10-i):
        print(end="       ")
    for j in range(10-i,10):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print()
