class Mymath:
    def __init__(self,r):
        self.r=r
    def perimeter(self):
        return 3.1415926*self.r*2
    def area(self):
        return 3.1415926*(self.r**2)
    def surface_area(self):
        return 4*3.1415926*(self.r**2)
    def volume(self):
        return (4*3.1415926*(self.r**3))/3


r=float(input("请输入球的半径："))
ball=Mymath(r)
print("圆的周长：{0:.2f}".format(ball.perimeter()))
print("圆的面积：{0:.2f}".format(ball.area()))
print("球的表面积：{0:.2f}".format(ball.surface_area()))
print("球的体积：{0:.2f}".format(ball.volume()))