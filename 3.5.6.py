years=range(2000,4001)
leapyears=[]
for year in years:
    if year%100!=0 and year%4==0:
        leapyears.append(year)
    elif year%100==0 and year%400==0:
        leapyears.append(year)
print('\n')
i=0
for leapyear in leapyears:
    print("{}".format(leapyear),end=" ")
    i+=1
    if i%9==0:
        print()
print("\n")