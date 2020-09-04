class X():
    def f(self):
        print('x')

class A(X):
    def f(self):
        print('a')
    def extra(self):
        print("extra a")

class B(X):
    def f(self):
        print('b')
    def extra(self):
        print("extra b")

class C(A,B,X):           
    def f(self):
        super(C,self).f()  #super函数将C类转换成了父类A
        print("c")

print("调用顺序")
print(C.mro())             #使用mro函数可知，C类的调用方式为广度优先搜索

c=C()
c.f()
c.extra()
