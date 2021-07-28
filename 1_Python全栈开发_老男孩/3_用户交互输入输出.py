# -*- coding:utf-8 -*-
"""
-------------------------------------------------用户交互输入-------------------------------------------------
注意：
1、input()会将用户输入的所有内容都存成字符串类型
2、int()只能将纯数字的字符串转换为整型（包含小数点也不支持）


-------------------------------------------------字符串的格式化输出-------------------------------------------------
一、%
1、值按照位置与%s一一对应，少一个不行，多一个也不行
    res = "my name is %s,my age is %s" % ('cyy', 24)
    print(res)

2、以字典的形式传入值，打破位置的限制
    res = "my name is %(name)s,my age is %(age)s" % {'name':'cyy', 'age':24}
    print(res)

二、str.format()
1、按照位置传值
    res = "my name is {},my age is {}".format('cyy', 24)
    print(res)

    res = "my name is {0},my age is {1}".format('cyy', 24)
    print(res)

2、以字典的形式传入值，打破位置的限制
    res = "my name is {name},my age is {age}".format(name='cyy', age=24)
    print(res)

三、f-string
1、python3.5之后推出的新方法
    x = input("请输入你的名字： ")
    y = input("请输入你的年龄： ")
    res = f' my name is {x},my age is {y} '
    print(res)

    res = f' my name is {{{x}}},my age is {y} '
    print(res)

2、可以在{}中放置任意合法的Python表达式，会在运行时计算
    print(f'{3*3-2}')

"""

