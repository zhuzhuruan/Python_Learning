# -*- coding:utf-8 -*-
"""
-------------------------------------------------while循环-------------------------------------------------
案例：

username = 'cyy'
password = '123'
count = 0
while count < 3:
    info_username = input("请输入您的用户名：")
    info_password = input("请输入您的密码：")
    if info_username == username and info_password == password:
        print("登录成功")
        while True:
            cmd = input("请根据提示输入您的指令：1-存款 ; 2-取款 ; 3-汇款 ; q:退出 : ")
            if cmd == 'q':
                break
            else:
                print("命令{x}正在运行".format(x=cmd))
        break
    else:
        print("用户名或密码错误")
        count += 1
else:
    print("输入错误超过3次，程序退出")



"""


username = 'cyy'
password = '123'
count = 0
while count < 3:
    info_username = input("请输入您的用户名：")
    info_password = input("请输入您的密码：")
    if info_username == username and info_password == password:
        print("登录成功")
        while True:
            cmd = input("请根据提示输入您的指令：1-存款 ; 2-取款 ; 3-汇款 ; q:退出 : ")
            if cmd == 'q':
                break
            else:
                print("命令{x}正在运行".format(x=cmd))
        break
    else:
        print("用户名或密码错误")
        count += 1
else:
    print("输入错误超过3次，程序退出")
