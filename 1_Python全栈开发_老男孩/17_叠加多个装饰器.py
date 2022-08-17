# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------叠加装饰器-------------------------------------------------
一、叠加装饰器的加载顺序和运行顺序
    
def deco1(func):            # func=被装饰对象index函数（wrapper2的内存地址）的内存地址
    def wrapper1(*args, **kwargs):
        print("正在运行====>deco1.wrapper1")
        res1 = func(*args, **kwargs)
        return res1

    return wrapper1


def deco2(func):            # func=被装饰对象index函数（wrapper3的内存地址）的内存地址
    def wrapper2(*args, **kwargs):
        print("正在运行====>deco2.wrapper2")
        res2 = func(*args, **kwargs)
        return res2

    return wrapper2


def deco3(z):
    def outer(func):        # func=被装饰对象index函数（原函数index）的内存地址
        def wrapper3(*args, **kwargs):
            print("正在运行====>deco3.outer.wrapper3", '===',z)
            res3 = func(*args, **kwargs)
            return res3

        return wrapper3

    return outer


# 加载顺序自下而上：deco3>deco2>deco1
@deco1                     # index=deco2(wrapper2的内存地址) ===> index=wrapper1的内存地址
@deco2                    # index=deco2(wrapper3的内存地址) ===> index=wrapper2的内存地址
@deco3('>')            # ===> @outer ===> index=outer(index) ===> index=wrapper3的内存地址
def index(x, y):
    print("from index %s:%s" % (x, y))
    return 'Successful'

print(index)


# 执行顺序自上而下：deco1>deco2>deco3
@deco1      # 传入wrapper2的内存地址，执行wrapper2，转到deco2
@deco2      # 转到deco2后，deco2传入的是wrapper3的内存地址，转到wrapper3
@deco3(">")        # 转到deco3,deco3传入的是index的内存地址，执行index
def index(x, y):
    print("from index %s:%s" % (x, y))
    return 'Successful'
res = index('aaa', 'zzz')
print(res)




-------------------------------------------------yield表达式-------------------------------------------------
# yield基本用法

def func():
    print('开始执行')
    cnt = 0
    while True:
        cnt += 1
        yield str('第'+str(cnt)+'次执行').center(50, '-')  
        print(str('第'+str(cnt)+'次执行完成').center(50, '=') )

func_iterator = func()
print(func_iterator.__next__())
print(func_iterator.__next__())


# yield的表达式形式

def func():
    print('开始执行')
    cnt = 0
    while True:
        cnt += 1
        name = yield    # 遇到yield暂停，执行上面的代码，并通过__next__()获得yield的返回值
        print(str(name + ':第'+str(cnt)+'次执行完成').center(50, '='))

func_iterator = func()
func_iterator.send(None)        # 等同于func_iterator.__next__()，yield传值需要初始化
func_iterator.send('测试程序1')
func_iterator.send('测试程序2')


# yield表达式形式和返回值结合使用
def func():
    print('开始执行')
    cnt = 0
    while True:
        cnt += 1
        name = yield 'Successful'.center(50, '~')   # 遇到yield暂停，执行上面的代码，并通过__next__()获得yield的返回值
        print(str(name + ':第'+str(cnt)+'次执行完成').center(50, '='))

func_iterator = func()
print(func_iterator.send(None))     # 初始化，传入None给yield,通过yield把None传给name,暂停程序
print(func_iterator.send('测试程序1'))    # 定位到上次暂停的位置，把'测试程序1'通过yield传给name,然后执行剩余的代码，直到再次遇到yield暂停
print(func_iterator.send('测试程序2'))    # 定位到上次暂停的位置，把'测试程序1'通过yield传给name,然后执行剩余的代码，直到再次遇到yield暂停



-------------------------------------------------三元表达式-------------------------------------------------
# 语法格式：条件成立时返回值 if 条件 else 条件不成立时返回值

# 普通格式
def func(x, y):
    if x>y:
        return x
    else:
        return y

max = func(1, 2)
print(max)


# 三元表达式
x = 1
y = 2
max = x if x>y else y
print(max)


-------------------------------------------------其他生成式-------------------------------------------------
一、列表生成式
# 语法格式: 循环可迭代对象，将其中满足条件的元素添加进新列表中
          [满足条件的元素 for 元素 in 可迭代对象 if 条件]
          [满足条件的元素 for 元素 in 可迭代对象] ====> [满足条件的元素 for 元素 in 可迭代对象 if True]


# 一般格式
lst = ['aaa_v', 'bbb', 'ccc_v', 'dddd']
new_lst = []
for i in lst:
    if i.endswith('_v'):
        new_lst.append(i)
print(new_lst)


# 列表生成式
lst = ['aaa_v', 'bbb', 'ccc_v', 'dddd']
new_lst = [i for i in lst if i.endswith('_v')]
print(new_lst)

lst = ['aaa_v', 'bbb', 'ccc_v', 'dddd']
upper_lst = [item.upper().strip('_V') for item in lst]
print(upper_lst)


二、字典生成式
dic_key = ['name', 'age', 'gender']
new_dic = {key: None for key in dic_key}
print(new_dic)

dic_key = [('name', 'cyy'), ('age', 18), ('gender', 'female')]
new_dic = {key:value for key, value in dic_key if key != 'gender'}
print(new_dic)


三、集合生成式
set_key = ['name', 'age', 'gender']
new_set = {item for item in set_key}
print(new_set)

注意：没有元组生成式，因为生成式这种形式其实是进行append的一个操作，元组没有append


四、生成器表达式
# 用()表示生成器表达式
num_iterator = (i for i in range(10) if i % 2 == 0)
while True:
    try:
        print(num_iterator.__next__())
    except StopIteration:
        break


# 案例：获取文件的字符长度
    # 方案一:循环每行叠加
        with open('17_叠加多个装饰器.py', 'rt', encoding='utf-8') as f:
            len_of_line = 0
            for line in f:
                len_of_line += len(line)
        print(len_of_line)
    
    # 使用列表生成式结合sum()叠加，缺点是如果行数过多，那么列表中的元素太多
        with open('17_叠加多个装饰器.py', 'rt', encoding='utf-8') as f:
            len_of_line = sum([len(line) for line in f])
        print(len_of_line)
    
    # 使用生成器表达式
        with open('17_叠加多个装饰器.py', 'rt', encoding='utf-8') as f:
            len_of_line = sum((len(line) for line in f))
        print(len_of_line)
    

"""

