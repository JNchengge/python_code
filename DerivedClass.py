class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hi(self):
        print("您好，我叫{0}，{1}岁".format(self.name,self.age))

class Student:
    def __init__(self,name,age,id):
        Person.__init__(self,name,age)
        self.id=id
    def say_hi(self):
        Person.say_hi(self)
        print("我是学生，我的学号为:",self.id)

p1=Person('张王一',33)
p1.say_hi()
s1=Student('李姚二',20,'201801001')
s1.say_hi()
