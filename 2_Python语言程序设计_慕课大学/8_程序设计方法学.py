# -*- coding:utf-8 -*-
import os.path
import time
from random import random

"""
---------------------------------------------------------知识点---------------------------------------------------------
"""

"""
-----------------------------第三方库----------------------------
安装Python第三方库
    -- 使用pip命令
        -- pip install -U <第三方库名>       # 更新已安装的指定第三方库
        -- pip uninstall <第三方库名>        # 卸载指定第三方库
        -- pip download <第三方库名>         # 下载但不安装指定的第三方库
        -- pip show <第三方库名>             # 列出某个指定第三方库的详细信息
        -- pip search <关键词>              # 根据关键词在名称和介绍中搜索第三方库
        -- pip list                        # 列出当前系统已经安装的第三方库        
    -- 集成安装方法
    -- 文件安装方法
        -- 为什么有些第三方库用pip可以下载，但无法安装？
            -- 某些第三方库pip下载后，需要编译再安装    
  
  
-----------------------------OS库----------------------------
os库提供通用的、基本的操作系统交互功能
    -- os库是Python标准库，包含几百个函数
    -- 常用路径操作、进程管理、环境参数等几类
        -- 路径操作：os.path子库，处理文件路径及信息
        -- 进程管理：启动系统中的其他程序
        -- 环境参数：获得系统软硬件信息等环境参数
        
路径操作: os.path子库以path为入口，用于操作和处理文件路径
    -- os.path.abspath(path): 返回path在当前系统中额绝对路径
    -- os.path.normpath(path): 归一化path的表示形式，统一用\\分隔路径
    -- os.path.relpath(path): 返回当前程序与文件之间的相对路径（relative path）
    -- os.path.dirname(path): 返回path中的目录名称
    -- os.path.basename(path): 返回path中最后的文件名称
    -- os.path.join(path, *paths): 组合path与paths，返回一个路径字符串
    -- os.path.exists(path): 判断path对应的文件或目录是否存在，返回True或False
    -- os.path.isfile(path): 判断path所对应是否为已存在的文件，返回True或False
    -- os.path.isdir(path): 判断path所对应是否为已存在的目录，返回True或False       
    -- os.path.getatime(path): 返回path对应文件或目录上一次的访问时间
    -- os.path.getmtime(path): 返回path对应文件或目录最近一次的修改时间
    -- os.path.getctime(path): 返回path对应文件或目录的创建时间   
    -- os.path.getsize(path): 返回path对应文件的大小，以字节为单位
    
进程管理: os.system(command)
    -- 执行程序或命令command
    -- 在Windows系统中，返回值为cmd的调用返回信息
    
环境参数：获取或改变系统环境信息
    -- os.chdir(path): 修改当前程序操作的路径
    -- os.getcwd(): 返回程序的当前路径
    -- os.getlogin(): 获得当前系统登录用户名称
    -- os.cpu_count(): 获得当前系统的CPU数量
    -- os.urandom(n): 获得n个字节长度的随机字符串，通常用于加密计算

"""
"""
---------------------------------------------------------实例---------------------------------------------------------
"""


# 体育竞技分析
def printIntro():  # 介绍性内容，提高用户体验
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


def getInputs():  # 获得用户输入
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值(0-1): "))
    n = eval(input("模拟比赛的场次: "))
    return a, b, n


def simOneGame(probA, probB):  # 模拟一场比赛
    scoreA, scoreB = 0, 0
    serving = "A"  # 发球方
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:  # 难度小于A的能力值
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


def simNGames(n, probA, probB):  # 模拟n场比赛
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA < scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def gameOver(a, b):  # 比赛结束
    return a == 15 or b == 15


def printSummary(winsA, winsB):  # 获得比赛结果
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA / n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB / n))


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


# 路径
def os_path():
    print(os.path.abspath("2_Python语言程序设计_慕课大学\\4_函数.py"))
    print(os.path.normpath("/2_Python语言程序设计_慕课大学//2_Python语言程序设计_慕课大学//4_函数.py"))
    print(os.path.relpath("4_函数.py"))
    print(os.path.dirname("/2_Python语言程序设计_慕课大学//2_Python语言程序设计_慕课大学//4_函数.py"))
    print(os.path.basename("/2_Python语言程序设计_慕课大学//2_Python语言程序设计_慕课大学//4_函数.py"))
    print(os.path.join("D:\\", "PYE\\file.txt"))
    print(os.path.exists("D:\\PYE\\file.txt"))
    print(os.path.isfile("D:\\PYE\\file.txt"))
    print(os.path.isdir("D:\\PYE\\file.txt"))
    print(time.ctime(os.path.getatime("/2_Python语言程序设计_慕课大学")))
    print(time.ctime(os.path.getmtime("/2_Python语言程序设计_慕课大学")))
    print(time.ctime(os.path.getctime("/2_Python语言程序设计_慕课大学")))
    print(os.path.getsize("4_函数.py"))


# 进程
def os_system():
    os.system("C:\\Windows\\System32\\calc.exe")
    os.system("C:\\Windows\\System32\\mspaint.exe 分词文件\\fivestart.png")


# 环境变量
def os_envi():
    print(os.getcwd())
    print(os.getlogin())
    print(os.cpu_count())
    print(os.urandom(10))


# 第三方库自动安装
def BatchInstall():
    libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests", "wheel"}
    try:
        for lib in libs:
            os.system("pip install " + lib)
        print("Successful")
    except:
        print("Failed Somehow")


if __name__ == "__main__":
    # main()
    # os_path()
    # os_system()
    # os_envi()
    BatchInstall()
