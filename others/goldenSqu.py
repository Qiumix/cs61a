import turtle
import math


# 定义画多边形的函数
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


# 定义画弧线的函数
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


# 新建turtle对象实例
bob = turtle.Turtle()
# 向右移动300，箭头朝上，移动到画布右侧
bob.fd(300)
bob.lt(90)

# 以300为半径，开始画1/4圆
r = 300
for i in range(10):
# 螺线用红色
    bob.color('red')
# 画1/4圆
    arc(bob, r, 90)
# 直线用黑色
    bob.color('black')
    bob.lt(90)
    bob.fd(r)
    bob.bk(r)
    bob.rt(90)
# 更改半径，乘上黄金比例
    r = r * 0.618
turtle.mainloop()