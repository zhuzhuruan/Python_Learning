# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------迭代器-------------------------------------------------
一、什么是迭代器
1、定义：迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次的结果继续的，单纯的重复并不是迭代

        while True:                     # 单纯的重复
            name = input("请输入您的姓名:")
        
        count = 0    
        while count < 5:            # 迭代，每次重复都是基于上一次的结果
            print(count)
            count += 1


二、为什么要有迭代器
    
    迭代器是用来迭代取值的工具，而涉及到把多个值循环取出来的数据类型包括：列表、字符串、元组、字典、集合、文件等
    
        # 实现了迭代取值的目的，但是这种迭代取值的方式只适用于有索引的数据类型：列表、字符串、元组
        lst = ['apple', 'banana', 'orange']
        i = 0
        while i < len(lst):
            print(lst[i])
            i += 1    
    
    因此为了解决基于索引迭代取值的局限性，Python必须提供一种能够不依赖与索引的取值方式，这就是迭代器        
            
          
三、如何使用迭代器   
1、可迭代对象(可以扎转换成迭代器的对象)：但凡内置有__iter__方法的都称之为可迭代对象

    可迭代对象.__iter__(): 得到可迭代对象的迭代器对象

            ''.__iter__()
            [].__iter__()
            {}.__iter__()
            {}.__iter__()
            ().__iter__()
            with open('file.txt', 'rt', encoding='utf-8') as f:
                f.__iter__()
   
2、迭代器对象：内置有__next__()方法，并且内置有__iter()方法的对象
    
    （1）迭代器对象.__next__(): 得到迭代器的下一个值
    （2）迭代器对象.__iter__(): 得到迭代器本身
    
    问题：可迭代对象调用迭代器对象__iter__()方法是为了得到他对应的迭代器对象，但是迭代器对象调用__iter__()方法得到的是他本身，那么
         为什么迭代器对象要有__iter__()方法？
    解答：目的为了让for循环的工作原理统一起来。对于可迭代对象，可以通过可迭代对像._iter__()获得迭代器对象；如果对于的是迭代器对象，也可以
         通过迭代器对象.__iter__()来得到迭代器对象本身，这样就可以不需要对可迭代对象或者迭代器对象进行区分，统一原理
         for item in 可迭代对象.__iter__():
            pass
         
         for item in 迭代器对象.__iter__():
            pass
    
    总结：可迭代对象不是迭代器对象（不具备__next__()方法），迭代器对象是可迭代对象（具备__iter__()方法）    
        
3、调用可迭代对象的__iter__()方法，会将其转换成迭代器对象，再使用可迭代对象的__next__()方法，可以逐个获取可迭代对象的每个元素
        
        # 方式1
        dic = {'name':'cyy', 'age':18, 'gender':'female'}
        dic_iterator = dic.__iter__()
        # print(dic_iterator)
        print(dic_iterator.__next__())
        print(dic_iterator.__next__())
        print(dic_iterator.__next__())
        print(dic_iterator.__next__())          # StopIteration：超出可迭代对象的数量时，抛出异常
          
        
        # 优化
        dic = {'name':'cyy', 'age':18, 'gender':'female'}
        dic_iterator = dic.__iter__()
        while True:
            try:
                print(dic_iterator.__next__())
            except StopIteration:
                break
        
        # 问题
        dic = {'name':'cyy', 'age':18, 'gender':'female'}
        dic_iterator = dic.__iter__()
        while True:
            try:
                print(dic_iterator.__next__())
            except StopIteration:
                break
                
        while True:                 # 报错          
            try:                  
                print(dic_iterator.__next__())
            except StopIteration:
                break
                
        # # 对同一个迭代器迭代取值只能取一次，可以类比老母鸡，一只老母鸡一生只能下100个蛋，迭代一下下完这100个蛋，就不能再进行下一次了, 
            所以如果要再迭代一次，就要再转换一次迭代器对象   
                
        dic = {'name':'cyy', 'age':18, 'gender':'female'}
        dic_iterator = dic.__iter__()
        while True:
            try:
                print(dic_iterator.__next__())
            except StopIteration:
                break
                
        dic_iterator = dic.__iter__()        
        while True:             
            try:
                print(dic_iterator.__next__())
            except StopIteration:
                break


四、for循环的工作原理

# 需求：循环取出字典中的元素
        # 通过迭代器对象
        dic = {'name':'cyy', 'age':18, 'gender':'female'}
        dic_iterator = dic.__iter__()
        while True:
            try:
                print(dic_iterator.__next__())
            except StopIteration:
                break

        # 直接使用for循环
        dic = {'name':'cyy', 'age':18, 'gender':'female'}
        for key in dic:
            print(key)
        
# 工作原理：（1）通过dic.__iter__()得到一个迭代器对象
          （2）通过迭代器对象.__next__()得到一个返回值，并且把该返回值赋值给key
          （3）循环往复（2），知道抛出StopIteration异常，for循环会捕捉异常然后结束循环    
    
    
# 总结：（1）可迭代对象：字符串、列表、集合、字典、元组、文件
       （2）迭代器对象：文件(python规定的)
       
            ''.__iter__()
            [].__iter__()
            {}.__iter__()
            {}.__iter__()
            ().__iter__()
            with open('file.txt', 'rt', encoding='utf-8') as f:
                f.__iter__()
                f.__next__()


五、迭代器优缺点
1、优点
    （1）为序列和非序列类型提供了一种统一的迭代取值方式
    （2）惰性计算：迭代器对象表示的是一个数据流，可以只在需要时才去调用next来计算一个值，就迭代器本身来说，同一时刻内存中只有一个值，因而可以存放
                无限大的数据流，而对于其他容器类型，如列表，需要把所有的元素都存放在内存中，受内存大小的限制，可以存放的值得个数是有限的
                （但是我们上述说到的迭代器都是通过可迭代对象例如列表.__iter()方法生成的迭代器对象，列表本身的元素个数就已经受到了限制，和迭代器
                 本身可以存放无限大的数据流有矛盾，所以需要直接创建一个本身就是迭代器对象的东西，也就是自定义迭代器（生成器），见下章）

2、缺点
    （1）除非取尽，否则无法获取迭代器的长度
    （2）只能取下一个值，不能回到开始，更像是“一次性的”，迭代器产生的唯一目标就是重复执行next方法知道值取尽，否则就会停留在某个位置，等待下一次调用
        next；若是要再次迭代同个对象，只能重新调用iter方法去创建一个新的迭代器对象，如果有两个或者多个循环使用同一个迭代器，必然只会有一个循环能取
        到值。 
        
        
        
        
-------------------------------------------------生成器-------------------------------------------------
1、定义：使用了 yield 的函数被称为生成器（generator）。
       跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，调用函数并不会执行函数体代码，而是返回一个生成器对象，更简单点理解生成器就是一个迭代器。        
        
        def func():
            print()
            
  总结：在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
       调用一个生成器函数，返回的是一个迭代器对象。  
       
       有了yield关键字，就有了一种自定义迭代器的实现方式。yield可以用于返回值，但不同于return，函数一旦遇到return就结束了，而yield可以保存函数
       的运行状态挂起函数，用来返回多次值

        def func():
            print('第一次执行')
            yield 'First'.center(50, '-')       # 遇到yield暂停，执行上面的代码，并通过__next__()获得yield的返回值
            print('第二次执行')
            yield 'Second'.center(50, '-')
            print('第三次执行')
            yield 'Third'.center(50, '-')
            print('第四次执行')          # 没有yield，抛出StopIteration异常
        
        
        func_iterator = func()      # func_iterator是返回的迭代器
        res1 = func_iterator.__next__()
        print(res1)
        res2 = func_iterator.__next__()
        print(res2)
        res3 = func_iterator.__next__()
        print(res3)
        res4 = func_iterator.__next__()
        
        
------------------------------------案例--------------------------------------  
# 实现range()的功能   
def func(start, end, step):
    while start < end:
        yield start
        start += step

range_func = func(1, 5, 2)

while True:
    try:
        print(range_func.__next__())
    except StopIteration:
        break
   

# 斐波那契数列
import sys
def fibonacci(n):               # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a+b
        counter += 1

f = fibonacci(10)       # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(f.__next__(), end=" ")
    except StopIteration:
        sys.exit()


                    
"""

