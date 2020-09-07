class Temperature:
    def __init__(self,degree):
        self.degree=degree
    def ToFahrenheit(self):
        return (self.degree*9/5)+32
    def ToCelsius(self):
        return (self.degree-32)*5/9

c=float(input("请输入摄氏温度："))
t_c=Temperature(c)
print("摄氏温度：{0:.1f}，华氏温度：{1:.1f}".format(c,t_c.ToFahrenheit()))
f=float(input("请输入华氏温度："))
t_f=Temperature(f)
print("华氏温度：{0:.1f}，摄氏温度：{1:.1f}".format(f,t_f.ToCelsius()))