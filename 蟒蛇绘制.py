# 绘制蟒蛇
import turtle
# 显示窗体的宽度和高度，显示窗体相对于左上角的位置
turtle.setup(800,800)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(15)
# 改变颜色，255是整数模式，1.0是小数模式
turtle.colormode(1)
turtle.pencolor(1,1,0)
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()