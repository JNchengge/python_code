years=range(2000,3001)
leapyears=[]
for year in years:
    if year%100!=0 and year%4==0:
        leapyears.append(year)
    elif year%100==0 and year%400==0:
        leapyears.append(year)
for leapyear in leapyears:
    print("{}".format(leapyear),end=" ")
print("\n")