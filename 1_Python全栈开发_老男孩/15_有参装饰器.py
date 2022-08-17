# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------有参装饰器-------------------------------------------------
一、知识储备
    根据对装饰器模板的分析（语法糖），outer_func()和wrapper()的参数都不能变化
    
        from functools import wraps
        def outer_func(func):
            @wraps(func)            # 作为wrapper的装饰器，把原函数func的所有函数属性赋值给wrapper函数
            def wrapper(*args, **kwargs):
                '''装饰器代码'''
                res = func(*args, **kwargs)
                ...
                return res
        
            return wrapper
        
        @outer_func             # original_func = outer_func(original_func)
        def original_func():
            '''主函数代码'''
            pass
        
        original_func()


二、有参装饰器模板

        from functools import wraps
        def outer_func(parameter1, parameter2, parameter3):          
            def deco(func):  
                @wraps(func)          
                def wrapper(*args, **kwargs):
                    '''装饰器代码'''
                    res = func(*args, **kwargs)
                    ...
                    return res
            
                return wrapper
            return deco
        
        @outer_func(parameter1, parameter2, parameter3)            
        def original_func():
            '''主函数代码'''
            pass
        
        original_func()


------------------------------------------------需求案例----------------------------------------------

# 需求：基于不同的账号密码来源，进行登录确认（必须使用语法糖）

    # 原功能
    from functools import wraps
    def auth(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''添加认证功能'''
            name = input("请输入您的姓名：").strip()
            password = input("请输入您的姓名：").strip()
    
            with open("practice_file/文件的使用.txt", 'rt', encoding='utf-8') as f:
                for line in f:
                    user_in, pwd_in = line.strip().split(':')
                    if name == user_in and password == pwd_in:
                        print("Login Successful".center(50, '-'))
                        res = func(*args, **kwargs)             # 原函数
                        return res
                else:
                    print("user or password is error")
    
        return wrapper
    
    @auth
    def original_func():
        '''主函数代码'''
        print("程序正在执行过程中，请您耐心等待，谢谢配合！")
    
    # original_func = auth(original_func)
    original_func()

    
    # 解决方式一
    from functools import wraps

    def auth(db_type):
        def deco(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                '''添加认证功能'''
                name = input("请输入您的姓名：").strip()
                password = input("请输入您的姓名：").strip()
                if db_type == 'file':
                    '''基于文件来源的验证'''
                    with open("practice_file/文件的使用.txt", 'rt', encoding='utf-8') as f:
                        for line in f:
                            user_in, pwd_in = line.strip().split(':')
                            if name == user_in and password == pwd_in:
                                print("Login Successful".center(50, '-'))
                                res = func(*args, **kwargs)  # 原函数
                                return res
                        else:
                            print("user or password is error")
    
                elif db_type == 'mysql':
                    if name == '张三' and password == '123':
                        print("Login Successful".center(50, '-'))
                        res = func(*args, **kwargs)  # 原函数
                        return res
                    else:
                        print("user or password is error")
    
                else:
                    print('目前暂不支持该文件来源'.center(50, '-'))
    
            return wrapper
    
        return deco
    
    
    deco = auth(db_type='file')             # 每一次都给deco先传值，再使用
    
    @deco
    def original_func():
        '''主函数代码'''
        print("程序正在执行过程中，请您耐心等待，谢谢配合！")
    
    
    original_func()


    # 解决方案三：有参装饰器
    from functools import wraps
    
    
    def auth(db_type):
        def deco(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                '''添加认证功能'''
                name = input("请输入您的姓名：").strip()
                password = input("请输入您的姓名：").strip()
                if db_type == 'file':
                    '''基于文件来源的验证'''
                    with open("practice_file/文件的使用.txt", 'rt', encoding='utf-8') as f:
                        for line in f:
                            user_in, pwd_in = line.strip().split(':')
                            if name == user_in and password == pwd_in:
                                print("Login Successful".center(50, '-'))
                                res = func(*args, **kwargs)  # 原函数
                                return res
                        else:
                            print("user or password is error")
    
                elif db_type == 'mysql':
                    if name == '张三' and password == '123':
                        print("Login Successful".center(50, '-'))
                        res = func(*args, **kwargs)  # 原函数
                        return res
                    else:
                        print("user or password is error")
    
                else:
                    print('目前暂不支持该文件来源'.center(50, '-'))
    
            return wrapper
    
        return deco
    
    
    @auth(db_type='file')       # 先执行deco=auth(db_type='file'),返回值deco给到@，相当于@deco，用@deco装饰原函数original_func()
    def original_func():
        '''主函数代码'''
        print("程序正在执行过程中，请您耐心等待，谢谢配合！")
    
    
    original_func()
    


"""
from functools import wraps


def auth(db_type):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''添加认证功能'''
            name = input("请输入您的姓名：").strip()
            password = input("请输入您的姓名：").strip()
            if db_type == 'file':
                '''基于文件来源的验证'''
                with open("practice_file/文件的使用.txt", 'rt', encoding='utf-8') as f:
                    for line in f:
                        user_in, pwd_in = line.strip().split(':')
                        if name == user_in and password == pwd_in:
                            print("Login Successful".center(50, '-'))
                            res = func(*args, **kwargs)  # 原函数
                            return res
                    else:
                        print("user or password is error")

            elif db_type == 'mysql':
                if name == '张三' and password == '123':
                    print("Login Successful".center(50, '-'))
                    res = func(*args, **kwargs)  # 原函数
                    return res
                else:
                    print("user or password is error")

            else:
                print('目前暂不支持该文件来源'.center(50, '-'))

        return wrapper

    return deco


@auth(db_type='file')       # 先执行deco=auth(db_type='file'),返回值deco给到@，相当于@deco，用@deco装饰原函数original_func()
def original_func():
    '''主函数代码'''
    print("程序正在执行过程中，请您耐心等待，谢谢配合！")


original_func()


