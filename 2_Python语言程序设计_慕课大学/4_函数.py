# -*- coding:utf-8 -*-
"""
---------------------------------------------------------知识点---------------------------------------------------------
"""
"""
-----------------------------函数的定义----------------------------
函数是一段代码的表示：
    -- 函数是一段具有特定功能的、可重用的语句组
    -- 函数是一种功能的抽象，一般函数表达特定功能
    -- 两个作用：降低编程难度和代码复用

y = f(x):
    -- 函数定义时，所指定的参数是一种占位符
    -- 函数定义后，如果不经过调用，不会被执行
    -- 函数定义时，参数是输入、函数体是处理，结果是输出（IPO）

可选参数传递：函数定义时可以为某些参数指定默认值，构成可选参数
    -- def <函数名>(<非可选参数>, <可选参数>):
            <函数体>
            return <返回值>

可变参数传递：函数定义时可以设计可变数量参数，既不确定参数总数量
    -- def <函数名>(<参数>, *b):
            <函数体>
            return <返回值>

参数传递的两种方式：
    -- 位置传递
    -- 名称传递    
    
函数的返回值：函数可以返回0个或多个结果            
    -- return保留字用来传递返回值
    -- 函数可以有返回值，也可以没有，可以有return，也可以没有
    -- return可以传递0个返回值，也可以传递任意多个返回值(元组类型)
    
    
-----------------------------局部变量和全局变量----------------------------
规则1：局部变量和全局变量是不同变量
    -- 局部变量是函数内部的占位符，与全局变量可能重名但不同
    -- 函数运算结束后，局部变量被释放
    -- 可以使用global保留字在函数内部使用全局变量
    
规则2：局部变量为组合数据类型且未创建，等同于全局变量

使用规则：
    -- 基本数据类型，无论是否重名，局部变量与全局变量不同
    -- 可以通过global保留字在函数内部声明全局变量
    -- 组合数据类型，如果局部变量未真实创建，则是全局变量
    
    
-----------------------------lambda函数----------------------------
lambda函数返回函数名作为结果
    -- lambda函数是一种匿名函数，即没有名字的函数
    -- 使用lambda保留字定义，函数名是返回结果
    -- lambda函数用于定义简单的、能够在一行内表示的函数
    -- <函数名> = lambda<参数>：表达式
                等价于
       def <函数名>(<参数>):
           <函数体>
           return <返回值>

谨慎使用lambda函数
    -- lambda函数主要用作一些特定函数或方法的参数
    -- lambda函数有一些固定使用方式
    -- 一般情况下，建议使用def定义的普通函数
                 
"""


"""
---------------------------------------------------------实例---------------------------------------------------------
"""


# 可变参数
def variable_parameter(n, *b):
    s = 1
    for i in range(1, n + 1):
        s *= i
    for item in b:
        s *= item
    return s


# 局部变量和全局变量
n, s = 10, 100          # 这里的s是全局变量
def fact1(n):
    s = 1           # 这里的s是局部变量
    for i in range(1, n + 1):
        s *= i
    return s
print(fact1(n), s)


n, s = 10, 100          # 这里的s是全局变量
def fact2(n):
    global s
    s = 1           # 这里的s是局部变量
    for i in range(1, n + 1):
        s *= i
    return s
print(fact2(n), s)


ls = ['F', 'f']
def func(a):
    ls.append(a)
    return
func('C')
print(ls)


ls = ['F', 'f']
def func(a):
    ls = []
    ls.append(a)
    return
func('C')
print(ls)


f = lambda x, y: x+y

if __name__ == "__main__":
    # if_else_case()
    # try_except_case()
    # for_else_case()
    # random_case()
    s = variable_parameter(10, 3, 6, 8)
    print(s)
    a = f(10, 15)
    print(a)

