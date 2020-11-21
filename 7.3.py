import sys
class NumberError(Exception):
    def __init__(self,data):
        Exception.__init__(self,data)
        self.data=data
    def __str__(self):
        return self.data+'：成绩不能为负数！请重新输入！'

class RangeError(Exception):
    def __init__(self,data):
        Exception.__init__(self,data)
        self.data=data
    def __str__(self):
        return self.data+'：超出1-100的范围，请重新输入！'

def get_score():
    try:
        a=int(sys.argv[1])
    except ValueError:
        print("输入的不是数字，请重新输入！")
        exit(0)
    if a<0:
        raise NumberError(str(a))
    elif a>100:
        raise RangeError(str(a))

get_score()