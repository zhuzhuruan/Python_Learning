# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------函数-------------------------------------------------
一、函数的定义
1、定义函数
    （1）申请内存空间保存函数体代码
    （2）将内存地址绑定函数名
    （3）定义函数不会执行函数体代码，但是会检查函数体语法

2、定义函数的三种形式
    （1）无参函数
    （2）有参函数
    （3）空函数：函数体代码为pass,通常用于构思代码
            def func():
                pass

二、函数的调用
1、调用函数
    （1）通过函数名找到函数的内存地址
    （2）通过函数名()的形式触发函数体代码的执行

三、函数的参数
（一）形参与实参的定义
    1、形参：在定义函数阶段定义的参数称之为形式参数，简称形参（相当于变量名）
    2、实参：在调用函数阶段传入的值称之为实际参数，简称实参（相当于变量值）
    3、形参与实参的关系：在调用阶段，实参（变量值）的内存地址会绑定给形参（变量名），这种绑定关系只能在函数体内使用，并且在函数调用时生效，函数调用结束后解除绑定关系

（二）形参与实参的具体使用
    1、位置参数：按照从左到右的顺序依次定义的参数
        特点：必须被传值，形参和实参一一对应，多一个少一个都不行
    2、关键词参数：按照key=value的形式传值
        特点：可以不参照顺序，直接按照形参=实参的形式传值
    3、位置参数和关键词参数一起使用
        （1）位置实参必须放在关键词实参的前面
        （2）不能为同一个形参重复传值
    4、默认参数：在定义函数阶段，就已经被赋值的形参
        特点：在定义阶段就已经被赋值，因此在调用阶段可以不用为其赋值
    5、位置形参和默认形参一起使用
        （1）位置参数必须在默认参数的前面
        （2）默认参数的值是在函数定义阶段被赋值的，准确的说被赋予的是值得内存地址
        （3）虽然默认值可以被指定为任意数据类型，但是不推荐使用可变类型
            m = 2
            def func(x ,y=m):
                print(x, y)
            m = 33
            func(1)

            m = ['aaa',]
            def func(x, y=m):
                print(x, y)
            m.append('bbb')
            func(1)

    （三）可变长度的参数（*与**的用法）
        1、定义：可变长度指的是在调用函数时，传入的值（实参）的个数不固定，而实参是用来为形参赋值的，所以对应着，针对溢出的实参必须有对应的形参来接收
        2、分类：*与**
            （1）*
                1）用来接收溢出的位置实参，溢出的位置实参会被*保存成元组的格式，然后赋值给紧跟其后的参数名(规范性命名：args)
                    def func(x, y, *args):      
                        print(x, y, args)
                    func(1,2,3,4,5,6,7,8)
                2）可以用在实参中，实参中紧跟*后的实参会被拆分成位置实参（*后紧跟的实参是可循环取值的类型）
                    def func(x, y, z):
                        print(x, y, z)
                    func(*[1,2,3])
                3）形参和实参中可以同时包含*
                    def func(x, y, *args):
                        print(x, y, args)
                    func('hi', 'hey', *'hello')       
            （2）**
                1）用来接收溢出的关键词实参，溢出的关键字实参会被**保存成字典的格式，然后赋值给紧跟其后的参数名（规范性命名：kwargs）
                    def func(x, y, **kwargs):
                        print(x, y, **kwargs)
                    func(1, 2, name='cyy', age=23)
                2）可以用在实参中，实参中紧跟**后的实参会被拆分成关键字实参（**后紧跟的实参只能是字典类型）
                    def func(name, gender, age):
                        print(name, gender, age)
                    func(**{'name': 'cyy', 'gender': 'female', 'age': 23})   
                3）形参和实参中可以同时包含**
                    def func(name, gender, **kwargs):
                        print(name, gender, kwargs)
                    func(**{'name':'cyy', 'gender':'female', 'age':23, 'marital':'single'})
    
    （四）命名关键字参数
        1、定义：在定义函数时，在形参*后面定义的参数，称之为命名关键字参数
                def func(x, y, *, a, b):    # a、b是命名关键字参数
                    print(x, y)
                def func(x, y, *args, a, b):    # a、b是命名关键字参数
                    print(x, y)
        2、特点：命名关键字参数必须按照key=value的关键字形式
                def func(name, age, *, gender, marry_status):
                    print(name, age, gender, marry_status)
                func('cyy', 23, gender='female', marry_status='single')
    
    （五）组合使用：
        1、规则：位置形参、默认形参、可变位置形参、命名关键字形参、可变关键字形参
                def func(name, age=18, *args, gender, **kwargs):
                    print(name, age, args, gender, kwargs)


三、函数对象
1、定义：可以把函数当成变量去用
2、特点：
    （1）可以赋值
            def func1():
                print("Hello World")
            func2 = func1       # 函数的内存地址
            func2()
    
    （2）可以当做函数的参数传入
            def func():
                print("Hello World")
             
            def foo(x):
                print(x)
                x()
            
            foo(func)     
    
    （3）可以当做函数的返回值
            def func():
                print("Hello World")
            
            def foo(x):
                return x
                
            res = foo(func)
            print(res)
            res()
            
    （4）可以当做容器类型的元素
            def func():
                print("Hello World")
            lst = [func,]
            lst[0]()
            
            --------------------------------------案例--------------------------------------
            def login():
                print("登录功能")
            
            def transfer():
                print("转账功能")
            
            def check_balance():
                print("查询余额")
            
            def withdraw():
                print("提现功能")
            
            def register():
                print("注册功能")
            
            while True:
                print(""""""
                    0--------退出
                    1--------登录功能
                    2--------转账功能
                    3--------查询余额
                    4--------提现功能
                    5--------注册功能
                """""")
            choice = input("请输入命令编号：").strip()
            if not choice.isdigit():  
                print("您输入的格式有误，请输入命令编号")
                continue
                
            if choice == '0':
                break
            if choice == '1':
                login()
            elif choice == '2':
                transfer()
            elif choice == '3':
                check_balance()
            elif choice == '4':
                withdraw()
            elif choice == '5':
                register()
            else:
                print("您输入的命令不存在")
            
            --------------------------------------优化--------------------------------------
            def login():
                print("登录功能")
            
            
            def transfer():
                print("转账功能")
            
            
            def check_balance():
                print("查询余额")
            
            
            def withdraw():
                print("提现功能")
            
            
            def register():
                print("注册功能")
            
            
            func_dic = {'0':['退出',None], '1':['登录功能',login], '2':['转账功能',transfer], '3':['查询余额',check_balance], '4':['提现功能',withdraw], '5':['注册功能',register]}
            
            while True:
                for key, value in func_dic.items():
                    print(key, '------------', value[0])
                choice = input("请输入命令编号：").strip()
                if not choice.isdigit():
                    print("您输入的格式有误，请输入命令编号")
                    continue
                if choice == '0':
                    break
                if choice in func_dic:
                    func_dic[choice][1]()
            
            
四、函数嵌套
1、嵌套调用：在调用函数A的过程中又调用函数B
            def func1():
                ...
                func2()
                
2、嵌套定义：在定义函数A的过程中又定义函数B
            def func1():
                ...
                def func2():
                    pass
                    
            --------------------------------------案例--------------------------------------
            from math import pi
            def circle(radius, action):
                def perimeter(radius):
                    return 2 * pi * radius
            
                def area(radius):
                    return pi * (radius ** 2)
            
                if action == 0:
                    return perimeter(radius)
                elif action == 1:
                    return area(radius)
            
            res = circle(3, 1)
            print(res) 


       
"""

