print("0~1000中用3除余2，用5除余3，用7除余2的数有：")
for num in range(0,1001):
    if num%3==2 and num%5==3 and num%7==2:
        print(str(num),end=" ")
print("\n")