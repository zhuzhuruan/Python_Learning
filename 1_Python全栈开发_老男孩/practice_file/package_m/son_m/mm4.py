# -*- coding:utf-8 -*-
print('模块文件mm4.by'.center(100,'='))
# 文件名：foo.py
# print(__name__)

# 绝对导入
# from practice_file.package_m.mm1 import func1

# 相对导入
from ..mm1 import func1

def func4():
    print('功能4'.center(50, '~'))


def func5():
    print('调用函数f1()')
    func1()
