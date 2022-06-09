# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------函数递归-------------------------------------------------
一、定义
    （1）函数的递归调用：是函数嵌套调用的一种特殊形式，在调用函数过程中直接或间接的调用函数本身
    （2）递归的本质就是循环
    （3）递归调用不应该无限地调用下去，必须在满足某种条件的情况下结束递归调用

# 直接调用
def func1():
    print("Hello World!")
    func1()
    
# 间接调用
def func1():
    print("Hello World!")
    func2()
    
def func2():
    print("Hello Hello World!")
    func1()

# 递归的本质就是循环
    # 方案一：使用while循环一段代码
        while True:
            print("Hello World!")
            print("Hello Hello World!")
            print("Hello Hello Hello World!")
            
    # 方案二：使用递归调用一段代码
    def func():
        print("Hello World!")
        print("Hello Hello World!")
        print("Hello Hello Hello World!")
        func()
    func()    

# 满足条件的情况下结束递归调用
    # while方式
        n = 0
        while n < 10:
            print('序号：', n)
            n += 1
            
    # 递归方式
        def func(n):
            if n == 10:
                return 
            print(n)
            n += 1
            func(n)
        
        func(0)
        
        
 二、递归调用的两个阶段      
 1、回溯：一层一层的调用下去
 2、递推：满足某种结束条件，结束递归调用，然后一层一层返回
 
 
# 案例：询问A员工的薪水，A说比B多1000，B说比C多1000，C说比D多1000，D说比E多1000，E说薪资是5000
        # 回溯
            A = B + 1000
            B = C + 1000
            C = D + 1000
            D = E + 1000
            E = 5000
        
        # 递推
            E = 5000
            D = 5000 + 1000 = 6000
            C = 6000 + 1000 = 7000
            B = 7000 + 1000 = 8000
            A = 8000 + 1000 = 9000
            
        # 递归调用函数
            def salary(n):
                if n == 1:  # E的薪资
                    return 5000
                else:
                    return salary(n - 1) + 1000
            
            salary_of_n = salary(5)
            print(salary_of_n)  
        
            
# 案例：取出嵌套多层的列表中的每个元素
        lst = [1, 2, [3, [4, [5, [6, [7, 8, [9, [10]]]]]]]]
        # 普通循环
        for item in lst:
            if isinstance(item, list):
        
                for item_sun in item:           # 循环的内容就是代码本身
                    if isinstance(item_sun, list):
                        ...
                    else:
                        print(item_sun)
        
            else:
                print(item)
        
        # 递归调用
        def func(lst):
            for item in lst:
                if isinstance(item, list):
                    func(item)
                else:
                    print(item)
        func(lst)
     
        

                 
"""
