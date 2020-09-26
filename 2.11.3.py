radius=float(input("请输入球的半径:"))
area=float(4*3.1415*radius*radius)
volume=(4/3)*3.1415*radius*radius*radius
print(str.format("球的表面积为：{0:2.1f}，体积为：{1:2.1f}",area,volume))