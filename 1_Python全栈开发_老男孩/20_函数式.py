# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------函数式-------------------------------------------------
一、匿名函数lambda
1、定义有名函数
    func = 函数的内存地址
    def func(x, y):
        return x+y

2、定义匿名函数: lambda 参数2,参数2,...:expression
    lambda x,y:x+y   

3、调用匿名函数
    # 方式一
        res = (lambda x,y:x+y)(1,2)
        print(res)
        
    # 方式二
        func = lambda x,y:x+y
        res = func(1,2)
        print(res)
        
    注：这两种方式都不是匿名函数的应用方式，匿名函数用于临时调用一次的场景，更多的是将匿名函数与其他函数配合使用
    
    
二、匿名函数的应用
  # 需求：找出薪资最高的人
        # 前提：max()的工作依据：传入可迭代对象，将其转换为迭代器对象，将迭代器对象中的值逐个比较，取出最大值
                # 可迭代对象全是数值列表
                    max([1,2,3,4,5,6,7,8,9])
                # 可迭代对象是字典
                    max({'Mary':3000, 'Tom':5060, 'Jack':10000, 'Lily':2490})                    
                    =====> 迭代的其实是字典的key: max(['Mary','Tom','Jack','Lily'])   
                    =====> 返回值就是Tom
                # max(可迭代对象 ,key=比较依据)
                    def func(可迭代对象):
                        return value                        
                    max(可迭代对象, key=func)
                        把可迭代对象的元素逐个当做参数传入func()函数，把func()函数的返回值给key,让它作为可迭代对象元素比较的依据
        
        # 实现
            # 有名函数的方式
                salaries = {'Mary':3000, 'Tom':5060, 'Jack':10000, 'Lily':2490}
                def func(key):
                    return salaries[key]
                max_p = max(salaries, key=func)
                print(max_p)
            
            # 匿名函数的方式
                salaries = {'Mary':3000, 'Tom':5060, 'Jack':10000, 'Lily':2490}
                max_p = max(salaries, key=lambda key:salaries[key])
                print(max_p)
                
                salaries_sort_key = sorted(salaries, key=lambda key:salaries[key])
                print(salaries_sort_key)
                
                salaries_sort = sorted(salaries.items(), key=lambda item:item[1])
                print(salaries_sort)

                    
三、map函数
1、定义：map() 会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

2、语法格式：map(function, iterable)：将可迭代对象中的每个元素作为参数传给function函数，得到的结果成为生成器的元素

    # 列表生成器        
        lst = ['aaa', 'bbb', 'ccc', 'ddd']
        lst_v = [item + '_v' for item in lst]
        print(lst_v)
    
    
    # 生成器表达式
        lst = ['aaa', 'bbb', 'ccc', 'ddd']
        lst_v = (item + '_v' for item in lst)
        print(lst_v.__next__())
        print(lst_v.__next__())
    
    # map函数式
        lst = ['aaa', 'bbb', 'ccc', 'ddd']
        lst_v = map(lambda item:item+'_v', lst)         # map()得到的是生成器
        print(lst_v.__next__())
    

三、filter()函数
1、定义：filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列，序列的每个元
        素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
2、语法格式：filter(function, iterable)：将可迭代对象中的每个元素作为参数传给function函数，得到的结果成为生成器的元素  
        
    # 列表生成器
        lst = ['aaa', 'bbb_v', 'ccc', 'ddd_v']
        lst_v = [item for item in lst if item.endswith('_v')]
        print(lst_v)
    
    # 生成器表达式
        lst = ['aaa', 'bbb_v', 'ccc', 'ddd_v']
        lst_v = (item for item in lst if item.endswith('_v'))
        print(lst_v.__next__())
        print(lst_v.__next__())
    
    # filter函数式
        lst = ['aaa', 'bbb_v', 'ccc', 'ddd_v']
        lst_v = filter(lambda item: item.endswith('_v'), lst)  # filter()得到的是生成器
        print(lst_v.__next__())
        print(lst_v.__next__())


四、reduce()函数
1、定义：reduce() 函数会对参数序列中元素进行累积。函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function
      （有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。 

2、语法格式：reduce(function, iterable[, initializer])

        from functools import reduce
        res = reduce(lambda x,y:x+y, [1,2,3,4,5])
        print(res)
        res = reduce(lambda x,y:x+y, [1,2,3,4,5], 10)
        print(res)    

      
"""
from functools import reduce
res = reduce(lambda x,yy:x*y, range(1,21))
resn = reduce(lambda x,y:x*y, range(1,17))
x = 0.2**4
y = 0.8**16

print(res, resn)
print(x*y*(res/(24*resn)))







