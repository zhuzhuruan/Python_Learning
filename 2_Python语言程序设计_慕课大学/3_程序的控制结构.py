# -*- coding:utf-8 -*-
"""
---------------------------------------------------------知识点---------------------------------------------------------
"""
import random
from random import random
from time import perf_counter

"""
-----------------------------分支结构----------------------------
紧凑形式：适用于简单表达式的二分支结构
    -- <表达式1> if <条件> else <表达式2>
    
循环控制保留字
    -- break跳出并结束当前整个循环，执行循环后的语句
    -- continue结束当次循环，继续执行后续次数循环
    -- break和continue可以与for和while循环搭配使用

循环与else
    -- 当循环没有被break语句退出时，执行else语句块
    -- else语句块作为"正常"完成循环的奖励
    -- 这里的else用法与异常处理中的else用法相似
    
    for <循环变量> in <遍历结构>:
        <语句块1>
    else:
        <语句块2> 
    
    while <条件>:
        <语句块1>
    else:
        <语句块2>
"""

"""
-----------------------------异常处理----------------------------
异常处理的基本使用：
-- 不带异常类型
    try:
        <语句块1>
    except:
        <语句块2>

-- 带有异常类型
    try:
        <语句块1>
    except <异常类型>:
        <语句块2>
        
-- 高级使用
    try:
        <语句块1>
    except:
        <语句块2>
    else:
        <语句块3>            # else对应<语句块3>在不发生异常时执行
    finally:                # finally对应<语句块4>一定执行 
        <语句块4>
        
"""

"""
-----------------------------random库----------------------------
-- 伪随机数：采用梅森旋转算法生成的(伪)随机序列中元素
-- random库主要用于生成随机数
-- 使用random库：import random
-- 基本随机数函数
    -- seed(a=None)：初始化给定的随机数种子，默认为当前系统时间
    -- random()：生成一个[0,1.0]之间的随机小数
-- 扩展随机数函数
    -- randint(a,b)：生成一个[a,b]之间的整数
    -- randrange(m, n[,k])：生成一个[m,n]之间以k为步长的随机整数    
    -- getrandbits(k)：生成一个k比特长的随机整数
    -- uniform(a,b)：生成一个[a,b]之间的随机小数
    -- choice(seq)：从序列seq中随机选择一个元素
    -- shuffle(seq)：将序列seq中的元素随机排列，返回打乱后的序列
"""
"""
---------------------------------------------------------实例---------------------------------------------------------
"""


def if_else_case():
    guess = eval(input("请输入一个数:"))
    print("猜{}了".format("对" if guess == 99 else "错"))


def try_except_case():
    """
    标注异常类型后，仅响应该异常，异常类型名字等同于变量
    """
    try:
        num = eval(input("请输入一个数:"))
        print(num ** 2)
    except NameError:
        print("输入的不是数值")


def for_else_case():
    """
    continue + else
    """
    for c in "PYTHON":
        if c == "T":
            continue
        print(c, end="")
    else:
        print("\n正常退出")

    """
    break + else
    """
    for c in "PYTHON":
        if c == "T":
            break
        print(c, end="")
    else:
        print("\n正常退出")

    """
    没有break，continue
    """
    for c in "PYTHON":
        print(c, end="")
    else:
        print("\n正常退出")


def random_case():
    # 随机数种子
    # random.seed(10)

    # 基本随机数
    print(random.random())
    # 扩展随机数
    print(random.randint(10, 100))
    print(random.randrange(10, 100, 10))
    print(random.getrandbits(16))
    print(random.uniform(10, 100))
    print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(s)
    print(s)


# 圆周率的计算
def CalPiv():
    DARTS = 1000 * 1000
    hits = 0.0
    start = perf_counter()
    for i in range(1, DARTS + 1):
        x, y = random(), random()
        dist = pow(x ** 2 + y ** 2, 0.5)
        if dist <= 1.0:
            hits = hits + 1
    pi = 4 * (hits / DARTS)
    print("圆周率值是：{}".format(pi))
    print("运行时间是：{:.5f}s".format(perf_counter() - start))


if __name__ == "__main__":
    # if_else_case()
    # try_except_case()
    # for_else_case()
    # random_case()
    CalPiv()
