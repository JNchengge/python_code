class Person22:
    def say_hi(self,name):
        print("您好，我叫",self.name)
    def say_hi(self,name,age):
        print("hi,{0},年龄:{1}".format(name,age))

p22=Person22()
p22.say_hi('Lisa',22)
