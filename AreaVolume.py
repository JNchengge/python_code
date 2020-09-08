import math
def area(r):
    return math.pi*r*r
def volume(r):
    return (4*math.pi*r*r*r)/3

if __name__=='__main__':
    r=float(input("请输入半径："))
    print("圆半径：{0:.2f}".format(area(r)))
    print("球体体积：{0:.2f}".format(volume(r)))