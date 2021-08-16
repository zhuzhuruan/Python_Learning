# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------装饰器-------------------------------------------------
一、什么是装饰器
1、定义
    （1）"器"：指的是工具，可以定义为函数
    （2）"装饰"：指的是为其他事物增加额外的东西来点缀
    （3）"装饰器"：指的是定义一个函数（或类），该函数是用来为其他函数添加额外的功能的

2、为什么要有装饰器
    （1）开放封闭原则
        <1>开放：指的是对拓展功能是开放的
        <2>封闭：指的是对修改源代码是封闭的
    
    结论：装饰器就是在不修改被装饰器对象源代码以及调用方式的前提下，为被装饰对象添加新功能


二、如何使用装饰器
# 需求：在不修改get_info()函数源代码以及调用方式的前提下为其添加"统计运行时间"的功能

# 1-源代码
    import time
    def get_info(name, age):
        time.sleep(3)
        print("My name is %(name)s, age is %(age)s" % {'name': name, 'age': age})
    
    get_info('cyy', 18)    
    
    
# 解决方案一：违背了开放封闭原则
    """"""问题：没有修改被装饰对象的调用方式，但是修改了源代码""""""   
    import time
    def get_info(name, age):
        start = time.time()
        time.sleep(3)
        print("My name is %(name)s, age is %(age)s" % {'name': name, 'age': age})
        end = time.time()
        print("程序运行时间为：{}s".format(end-start))
    
    get_info('cyy', 18)


# 解决方案二：违背了开放封闭原则
    """"""问题：没有修改被装饰对象的源代码，但是修改了被装饰对象的调用方式""""""
    import time
    def get_info(name, age):
        time.sleep(3)
        print("My name is %(name)s, age is %(age)s" % {'name': name, 'age': age})
    
    def wrapper(name, age):
        start = time.time()
        get_info(name, age) 
        end = time.time()
        print("程序运行时间为：{}s".format(end-start))   

    wrapper('cyy', 18)


# 解决方案三：优化解决方案二
    """"""优化原因：当get_info()函数本身的源代码确实要修改时，参数数量也要增加时，wrapper()函数也要相应的改""""""
    import time
    def get_info(name, age, gender):  # 增加参数
        time.sleep(3)
        print("My name is %(name)s, gender is %(gender)s, age is %(age)s" % {'name': name, 'age': age, 'gender': gender})
    
    def wrapper(*args, **kwargs):
        start = time.time()
        get_info(*args, **kwargs)
        end = time.time()
        print("程序运行时间为：{}s".format(end - start))
    
    wrapper('cyy', 18, 'female')
    
  
# 解决方案四：优化解决方案三
    """"""优化原因：装饰器是为被装饰对象添加功能的函数，解决方案三中装饰器只能为get_info()函数添加功能，被写死了""""""
    
    注意：为了让被装饰对象灵活，把被装饰对象作为参数传入，由于目前wrapper()中传入的参数都是为了给被装饰对象作为函数使用的，所以不能在wrapper()中直接传入
        def wrapper(*args, **kwargs, func_name):
            start = time.time()
            func_name(*args, **kwargs)
            end = time.time()
            print("程序运行时间为：{}s".format(end - start))
    
    # 采用闭包函数传入参数
        def outer_func(func_name):
            def wrapper(*args, **kwargs):
                start = time.time()
                func_name(*args, **kwargs)
                end = time.time()
                print("程序运行时间为：{}s".format(end - start))
            return wrapper
        
        func = outer_func(get_info)                 # func接收的是wrapper()函数的内存地址
        func('cyy', 18, 'female')
        
    # 实现不修改被装饰对象调用方式的情况下，为被装饰对象添加功能
        import time
        def get_info(name, age, gender):  
            time.sleep(3)
            print("My name is %(name)s, gender is %(gender)s, age is %(age)s" % {'name': name, 'age': age, 'gender': gender})
        
        def outer_func(func_name):
            def wrapper(*args, **kwargs):
                start = time.time()
                func_name(*args, **kwargs)
                end = time.time()
                print("程序运行时间为：{}s".format(end - start))
            return wrapper
        
        get_info = outer_func(get_info)
        get_info('cyy', '18', 'female')


# 解决方案五：优化解决方案四
    """"""优化原因：当被装饰对象存在返回值时""""""
        import time
        def get_info(name, age, gender):  
            time.sleep(3)
            print("My name is %(name)s, gender is %(gender)s, age is %(age)s" % {'name': name, 'age': age, 'gender': gender})
            return {'name':name, 'age':age, 'gender':gender}
        
        def outer_func(func_name):
            def wrapper(*args, **kwargs):
                start = time.time()
                func_name(*args, **kwargs)
                end = time.time()
                print("程序运行时间为：{}s".format(end - start))
            return wrapper
        
        get_info = outer_func(get_info)         # get_info接收的其实是wrapper()函数的内存地址
        res = get_info('cyy', '18', 'female')       # 伪装的是调用原始的get_info()函数，其实是包裹了get_info()函数的wrapper()函数,而wrapper()函数没有返回值，所以返回None
        print(res)          

    # 修改：实现装饰器的完整功能
        import time
        def get_info(name, age, gender):  
            time.sleep(3)
            print("My name is %(name)s, gender is %(gender)s, age is %(age)s" % {'name': name, 'age': age, 'gender': gender})
            return {'name':name, 'age':age, 'gender':gender}
        
        def outer_func(func_name):
            def wrapper(*args, **kwargs):
                start = time.time()
                result = func_name(*args, **kwargs)         # 获取get_info()的返回值
                end = time.time()
                print("程序运行时间为：{}s".format(end - start))
                return result                   # 返回get_info()的返回值
            return wrapper
        
        get_info = outer_func(get_info)         # get_info接收的其实是wrapper()函数的内存地址
        res = get_info('cyy', '18', 'female') 
        print(res)      


# 解决方案六：
    '''在解决方案五中，通过get_info = outer_func(get_info)用get_info接收wrapper()函数的内存地址，伪装的和原函数get_info一样，但其实通过
        print(get_info)来查看内存地址时就露馅了，发现打印出来的其实是wrapper()函数里面的get_info函数的内存地址，并不是原函数get_info()函数
        原本的内存地址，print(get_info.__name__)、print(get_info.__doc__)等打印get_info函数属性其实也不是原函数get_info()的属性，所以
        需要把伪装成get_info()函数的wrapper()函数的属性都变成和原函数get_info()一致
    '''
    
    # 原装饰器模板
        def outer_func(func):
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
        print(original_func.__name__)           # 查看函数名字
        print(original_func.__doc__)            # 查看函数注释文档
                    
    
    # 修改1
    def outer_func(func):
        def wrapper(*args, **kwargs):
            '''装饰器代码'''
            res = func(*args, **kwargs)
            ...
            return res
        
        wrapper.__name__ = func.__name__                # 偷偷的将原函数func()的属性值赋值给wrapper()
        wrapper.__doc__ = func.__doc__
    
        return wrapper
    
    @outer_func             # original_func = outer_func(original_func)
    def original_func():
        '''主函数代码'''
        pass
    
    original_func()
    print(original_func.__name__)           # 查看函数名字
    print(original_func.__doc__)            # 查看函数注释文档
    
    
    # 修改2：修改1需要一一将函数属性赋值给wrapper函数，Python中提供了方法将函数所有属性值赋给另一个函数
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
    
    print(original_func.__name__)           # 查看函数名字
    print(original_func.__doc__)            # 查看函数注释文档
    
    

-------------------------------------------------语法糖-------------------------------------------------
# 建立了一个装饰器，通过传入不同的被装饰对象来为被装饰对象添加功能，但是每次都需要通过接收内存地址的方式来接收再调用，如何简洁使用呢？
'''
    语法糖：@outer：把@outer下面跟着的函数名当做唯一的参数值传给outer()
                  对于装饰器来说，就是outer函数只能有一个参数，并且该参数只能用来接收被装饰对象的内存地址
          @outer()：先执行函数outer()，再把outer()的执行结果传给@，接下来就和上述步骤一致
          
    @outer
    def func():
        pass
    
'''
        import time
        
        
        def outer_func(func_name):
            def wrapper(*args, **kwargs):
                start = time.time()
                result = func_name(*args, **kwargs)  # 获取get_info()的返回值
                end = time.time()
                print("程序运行时间为：{}s".format(end - start))
                return result  # 返回get_info()的返回值
        
            return wrapper
        
        
        @outer_func  # 替代get_info = outer_func(get_info) ，因此装饰器函数要写在被装饰对象函数的前面
        def get_info(name, age, gender):
            time.sleep(3)
            print("My name is %(name)s, gender is %(gender)s, age is %(age)s" % {'name': name, 'age': age, 'gender': gender})
            return {'name': name, 'age': age, 'gender': gender}
        
        
        @outer_func
        def get_address(address):
            print("My address is %s" % address)
            return {'address':address}
        
        # get_info = outer_func(get_info)         # get_info接收wrapper()函数的内存地址
        res_info = get_info('cyy', '18', 'female')
        res_adr = get_address('China')
        print(res_info)
        print(res_adr)
        


"""

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

print(original_func.__name__)           # 查看函数名字
print(original_func.__doc__)            # 查看函数注释文档


        

