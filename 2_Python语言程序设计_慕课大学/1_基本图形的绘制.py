# -*- coding:utf-8 -*-
import turtle


#  TempCovert.py
def TempCovert():
    TempStr = input("请输入带有符号的温度值：")
    if TempStr[-1] in ['F', 'f']:
        C = (eval(TempStr[0:-1]) - 32) / 1.8
        print("转换后的温度是{:.2f}C".format(C))
    elif TempStr[-1] in ['C', 'c']:
        F = 1.8 * eval(TempStr[0:-1]) + 32
        print("转换后的温度是{:.2f}F".format(F))
    else:
        print("输入格式错误")


def Turtle_knowledge():
    """
    turtle.setup(width, height, startx, starty)
        - setup()设置窗体的大小及位置
        - 4个参数中后两个可选（startx, starty是窗体相较于系统窗口的坐标位置）
        - setup()不是必须的

    turtle.goto(x,y)
        - 绝对坐标,以画布的中心为(0,0),海龟将移动到(x,y)的位置

    空间坐标体系
        - turtle.circle(r,angle)    以海龟的位置画弧度
        - turtle.fd()   以海龟的位置向前走
        - turtle.kd()   以海龟的位置向后走

    角度坐标体系
        - turtle.seth(angle)
        - seth()只改变海龟行进方向但不行进
        - angle为绝对度数

    海龟角度
        - turtle.left(angle)
        - turtle.right(angle)

    turtle的RGB色彩模式
        - 默认采用小数值、可切换为整数值
        - turtle.colormode(mode)
            - 1.0:RGB小数值模式
            - 255:RGB整数值模式
    """
    turtle.setup(1000, 600)
    turtle.goto(-60, -60)
    turtle.fd(100)
    turtle.circle(100, 90)
    turtle.seth(180)

    turtle.done()


def Turtle_case():
    turtle.setup(650, 350, 200, 200)
    turtle.penup()
    turtle.fd(-250)
    turtle.pendown()
    turtle.pensize(25)
    turtle.pencolor("purple")
    turtle.seth(-40)
    for i in range(4):
        turtle.circle(40, 80)
        turtle.circle(-40, 80)
    turtle.circle(40, 80 / 2)
    turtle.fd(40)
    turtle.circle(16, 180)
    turtle.fd(40 * 2 / 3)
    turtle.done()


def test():
    turtle.screensize(500, 500)
    turtle.pensize(8)  # 笔的粗细
    turtle.speed(3)
    turtle.colormode(255)
    turtle.color((128, 64, 0))
    turtle.penup()  # 落笔
    turtle.goto(248, -200)  # 移动画笔到坐标为(248, -200)的位置
    turtle.pendown()

    # 开始填充
    turtle.begin_fill()  # 填充颜色
    turtle.fillcolor((249, 199, 192))
    turtle.seth(145)
    turtle.forward(180)
    turtle.seth(30)
    turtle.circle(125, 30)
    turtle.left(10)
    turtle.circle(80, 80)
    turtle.circle(30, 40)
    turtle.circle(25, 20)
    turtle.circle(100, 20)
    first = turtle.pos()

    turtle.seth(-145)
    turtle.circle(100, 50)
    turtle.circle(20, 60)
    sec = turtle.pos()
    turtle.circle(30, 70)

    turtle.seth(45)
    turtle.circle(400, 13)

    turtle.penup()
    turtle.goto(first)
    turtle.pendown()
    turtle.seth(145)
    turtle.forward(80)
    turtle.seth(140)
    turtle.circle(30, 90)
    turtle.seth(-150)

    turtle.circle(180, 60)
    turtle.circle(140, 20)
    turtle.left(15)
    turtle.circle(100, 40)
    turtle.right(15)
    turtle.circle(60, 60)
    turtle.circle(180, 10)
    turtle.seth(-35)
    turtle.forward(200)
    turtle.end_fill()  # 填充颜色

    turtle.pu()
    turtle.goto(sec)
    turtle.pd()
    turtle.seth(-100)
    turtle.circle(-120, 10)
    turtle.seth(-150)
    turtle.circle(-130, 10)
    turtle.seth(-180)
    turtle.circle(-130, 10)
    turtle.circle(-140, 10)
    third = turtle.pos()
    turtle.circle(-130, 20)
    turtle.pu()
    turtle.goto(third)
    turtle.pd()
    turtle.seth(-120)
    turtle.circle(-100, 20)

    turtle.pu()
    turtle.goto(0, 135)
    turtle.pd()
    turtle.write("冲", font=("微软雅黑", 100, "normal"))

    turtle.pu()
    turtle.goto(-300, 0)
    turtle.write("冲", font=("微软雅黑", 100, "normal"))
    turtle.pd()

    turtle.pu()
    turtle.goto(-300, -300)
    turtle.write("冲", font=("微软雅黑", 100, "normal"))
    turtle.pd()
    turtle.ht()
    turtle.done()


def test1():
    turtle.screensize(960, 640)
    # 先绘制一个黄色的⚪：
    turtle.pensize(200)
    turtle.pencolor("yellow")
    turtle.circle(100, 360)
    # 绘制嘴巴：从嘴巴左边开始起笔，旋转180°
    turtle.penup()
    turtle.seth(90)
    turtle.fd(90)
    turtle.seth(180)
    turtle.fd(150)
    turtle.seth(270)
    turtle.pendown()
    turtle.pensize(5)
    turtle.pencolor("black")
    turtle.circle(150, 180)
    # 开始绘制眼睛的轮廓：
    turtle.penup()
    turtle.fd(90)
    turtle.seth(155)
    turtle.pendown()
    turtle.pensize(40)
    turtle.pencolor("white")
    turtle.circle(160, 45)
    turtle.penup()
    turtle.circle(160, -45)
    turtle.seth(180)
    turtle.fd(180)
    turtle.seth(155)
    turtle.pendown()
    turtle.circle(160, 45)
    # 开始绘制眼球部分：
    turtle.penup()
    turtle.seth(0)
    turtle.fd(20)
    turtle.pendown()
    turtle.pensize(16)
    turtle.pencolor("black")
    turtle.circle(8)
    turtle.penup()
    turtle.fd(180)
    turtle.pendown()
    turtle.circle(8)
    turtle.done()


if __name__ == "__main__":
    # TempCovert()
    # Turtle_knowledge()
    # Turtle_case()
    # test()
    test1()
    # print('say Hi to Bob\'s mother')
    # print('Hello there!\nHow are you?\nI \'m doing fine.')
    # print("hello \t python")
    # print(r'Hello there!\nHow are you?\nI \'m doing fine.')
    # print('Hello there!\\nHow are you?\\nI \'m doing fine.')

