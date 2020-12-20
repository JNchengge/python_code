class Shape:
    def __init__(self,color):
        self.color=color
    def getcolor(self):
        return self.color
class Rectangle(Shape):
    def __init__(self,a,b,color):
        Shape.__init__(self,color)
        self.a=a
        self.b=b
    def getarea(self):
        return self.a*self.b
    def getcolor(self):
        return self.color
class Circle(Shape):
    def __init__(self,r,color):
        Shape.__init__(self,color)
        self.r=r
    def getarea(self):
        return 3.14*(self.r**2)
    def getcolor(self):
        return self.color

rectangle=Rectangle(5,5,"red")
circle=Circle(2,"blue")
print(rectangle.getarea())
print(rectangle.getcolor())
print(circle.getarea())
print(circle.getcolor())