# --------------------------------------- 字符串 ------------------------------------------------
# 1.1 转义字符
print('"Isn\'t",they said.')
print('First Line.\nSecond Line.')
print('C:\some\name')  # \被转义，如果不想前置了 \ 的字符转义成特殊字符，可以使用 原始字符串 方式，在引号前添加 r 即可
print(r'C:\some\name')

# 1.2 跨行连续输入
print("""\
Usage: thingy [OPTIONS]
     -h                       
     -H hostname
"""
      )

# 1.3 切片：切片的开始总是被包括在结果中，而结束不被包括
#          理解：将索引视作指向字符 之间 ，第一个字符的左侧标为0，最后一个字符的右侧标为 n ，其中 n 是字符串长度。
word = 'Hello World!'
word[0:2]

# --------------------------------------- 列表 ------------------------------------------------
# 1.1 形式：list = [, , , ,]

squares = [1, 2, 3, 4, 5, 6]
squares[0:4]  # 切片返回list
squares[:]  # 返回列表的一个浅拷贝
squares + [7, 8, 9, 10]  # 列表的拼接

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64  # mutable

# 1.2 .append()
cubes.append(216)
cubes.append(7 ** 3)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']  # 给切片赋值,甚至可以改变列表的大小，清空列表
letters[2:5] = []
letters[:] = []

# 1.3 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

# --------------------------------------- 浅拷贝和深度拷贝 ------------------------------------------------
# 直接赋值：其实就是对象的引用（别名）。
# 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
# 深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
import copy

a = {1: [1, 2, 3]}
b = a.copy()  # 浅拷贝
print(a, b)

a[1].append(4)
print(a, b)  # 浅拷贝：地址不变，地址指向的值变化，浅拷贝的对象变化

c = copy.deepcopy(a)
print(c)
a[1].append(5)
print(a, b, c)  # 深度拷贝，两个对象完全独立

# --------------------------------------- 流程控制语句 ------------------------------------------------

words = ['cat', 'window', 'defenestrate']
for i in words:
    print(i)

word = 'defenestrate'
for i in word:
    print(i)

# break 和 continue ：break跳出循环    continue继续循环中的下一次迭代

for i in 'python':
    if i == 'y':
        print('yes' + ':' + i)
        break
    else:
        print('no' + ':' + i)

for i in 'python':
    if i == 'y':
        print('yes' + ':' + i)
        continue
    else:
        print('no' + ':' + i)

# pass 语句：pass语句什么也不做。当语法上需要一个语句，但程序需要什么动作也不做时，可以使用它
while True:
    pass


# --------------------------------------- 定义函数 ------------------------------------------------
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

# 1.1 函数实例
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()  # 直接返回值


def fib2(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result  # 返回return列表


# 1.2 函数定义的更多形式
# 1.2.1 参数默认值
def ask_ok(promot, retries=4, reminder='Please try again'):
    while True:
        ok = input(promot)
        if ok in ('y', 'ye', 'yes'):  # in 测试一个序列是否包含某个值
            return True
        if ok in ('n', 'no', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# 1.2.2 关键字参数: 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# 1.2.3 不定长参数:需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名
#                *name:  加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
#                **name: 加了两个星号 ** 的参数会以字典的形式导入。
def test0(a, b, *args):
    print(a)
    print(b)
    print(args)  # 输出元组tuple


def test1(a, b, **vardict):
    print(a)
    print(b)
    print(vardict)
    print(vardict[1])


# 实例1
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# 实例2
def make_pizza(*toppings):  # *toppings创建了一个名为toppings的空元组
    print("\nMake pizza need following toppings: ")
    for topping in toppings:
        print("-" + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 实例3
def build_profile(first, last, **user_info):
    profile = {}
    profile['firstname'] = first
    profile['lastname'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


# 1.2.4 特殊参数
def standard(arg):  # 对调用方式没有任何限制，可以通过位置参数，也可以使用关键字参数
    print(arg)


# def pos_only_arg(arg, /):       # 通过 / 限制仅使用位置形参
#     print(arg)

def kwd_only_arg(*, arg):  # 通过 * 指明仅允许关键字参数
    print(arg)


# def combined_example(pos_only, /, standard, *, kwd_only):           # 同时限制位置参数和关键字参数
#      print(pos_only, standard, kwd_only)


# 1.2.5 解包参数列表
list(range(3, 6))

args = [3, 6]
list(range(*args))  # 通过 * 操作符从元组或列表中解包元组参数


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)  # 通过 ** 操作符从元组或列表中解包列表参数

# 1.2.6 Lambda表达式: 创建匿名函数, 这个函数返回两个参数的和： lambda a, b: a+b

sum = lambda arg1, arg2: arg1 + arg2


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)  # 传入n
f(1)  # 传入x

# --------------------------------------- 全局变量和局部变量 ------------------------------------------------
# 变量的作用域:
# 一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
# 变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：全局变量; 局部变量

# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

total = 0  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)
