# -*- coding:utf-8 -*-
import turtle

"""
---------------------------------------------------------知识点---------------------------------------------------------
"""

"""
-----------------------------模块化设计----------------------------
分而治之
    -- 通过函数或对象封装将程序划分为模块及模块间的表达
    -- 具体包括：主程序、子程序和子程序间关系
    -- 分而治之：一种分而治之、分层抽象、体系化的设计思想
紧耦合和松耦合
    -- 紧耦合：两个部分之间交流很多，无法独立存在
    -- 松耦合：两个部分之间交流很少，可以独立存在
    -- 模块内部紧耦合，模块之间松耦合    

    
---------------------------------递归-----------------------------
递归的定义：调用函数自身的方式
    两个关键特征：
        -- 链条：计算过程存在递归链条
        -- 基例：存在一个或多个不需要再次递归的基例
         
递归的实现：函数 + 分支语句
    n! = 1          n = 0
         n(n-1)!    otherwise
    
    -- 递归本身是一个函数，需要函数定义方式描述
    -- 函数内部，采用分支语句对输入参数进行判断
    -- 基例和链条，分别编写对应代码         
             

---------------------------------PyInstaller-----------------------------
将源文件打包生成可执行文件
    -- -h：查看帮助
    -- -clean: 清理打包过程中的临时文件
    -- -D，--onedir: 默认值，生成dist文件夹
    -- -F，--onedir: 在dist文件夹中只生成独立的打包文件
    -- i<图标文件名.ico>: 指定打包程序使用的图标（icon）文件

例：pyinstaller -i curve.ico -F SevenDigitsDrawV2.py    
    

"""
"""
---------------------------------------------------------实例---------------------------------------------------------
"""


# 求n!
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


# 九九乘法表
def nine():
    for i in range(1, 10):
        for j in range(1, 10):
            if i >= j:
                print("{}*{}={}".format(j, i, i * j), end=" ")
        print("\n")


# 将字符串反转s[::-1]
def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:]) + s[0]


# 斐波那契数列：F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)  （n≥2，n∈N*）
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


# 汉诺塔
count = 0


def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{} -> {}".format(1, src, dst))
        count += 1
    else:
        hanoi(n - 1, src, mid, dst)
        print("{}:{} -> {}".format(n, src, dst))
        count += 1
        hanoi(n - 1, mid, dst, src)


# 科赫雪花小包裹
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3       # 科赫雪花的阶数
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    # result = fact(10)
    # print(result)
    # nine()
    # result = rvs('abcd')
    # print(result)
    # hanoi(3, "A", "C", "B")
    # print(count)
    main()
