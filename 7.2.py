class SrtingError(Exception):
    def __init__(self,data):
        Exception.__init__(self,data)
        self.data=data
    def __str__(self):
        return "捕获异常"+self.data+'：出现大写字母'

a='Abcd'
if 'A' in a:
    raise SrtingError('A')