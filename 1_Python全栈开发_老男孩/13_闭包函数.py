# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------闭包函数-------------------------------------------------
一、什么是闭包函数
1、引入：
    （1）闭包函数 = 名称空间与作用域 + 函数嵌套 + 函数对象
    （2）核心点：命名空间的查找关系是以函数定义阶段为准的
    
2、定义：
    （1）"闭"：指的是该函数是内嵌函数
                def func1():
                    ...
                    def func2():
                        pass
    （2）"包": 指的是该函数包含对外层函数作用域名字的引用（不是对全局作用域）
                def func1():
                    x = 'aaa'
                    ...
                    def func2():
                        print(x)
                    func2()

    ----------------------------------------------案例：名称空间+作用域、函数嵌套---------------------------------------------
        def func1():
            x = 'aaa'
            def func2():
                print(x)
            func2()
        
        func1()
    ----------------------------------------------案例：函数对象---------------------------------------------
        def func1():
            x = 'aaa'
            def func2():
                print(x)
            return func2
        
        f = func1()
        f()
    
    
二、为什么要有闭包函数：为函数传参提供了一种新方式 
1、方式一：直接将变量传给函数
        def func(x):
            print(x)
            
        ----------------------------------案例-------------------------------
        import requests

        def get(url):
            response = requests.get(url)
            print(response.text)
        
        get("http://www.baidu.com")


2、方式二：闭包函数
        def func1(x):
            def func2():
                print(x)
        
            return func2
        
        func = func1('aaa')
        func()    
    
    
        ----------------------------------案例-------------------------------
        import requests
    
        def outer(url):
            def get():
                response = requests.get(url)
                print(response.text)
            return get
        
        baidu = outer("http://www.baidu.com")
        baidu()




"""


