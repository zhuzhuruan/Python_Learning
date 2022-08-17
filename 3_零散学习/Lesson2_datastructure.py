# --------------------------------------- 列表 ------------------------------------------------
# 1.1 列表的特性
fruits = ['oranges', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')  # 返回元素 x 在列表中出现的次数
fruits.index('banana')  # 返回列表中第一个值为 x 的元素的从零开始的索引
fruits.index('banana', 4)  # list.index(x[, start[, end]])可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列
fruits.reverse()  # 反转列表中的元素
fruits.append('graphs')  # 在列表的末尾添加一个元素
fruits.sort()  # 对列表中的元素进行排序
fruits.pop()  # 删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop() 将会删除并返回列表中的最后一个元素
fruits.insert(2, 'pear')  # 在给定的位置插入一个元素

# 1.2 列表作为栈使用: 要添加一个元素到堆栈的顶端，使用 append() 。要从堆栈顶部取出一个元素，使用 pop() ，不用指定索引
fruits.append('strawberry')
fruits.pop()

# 1.3 del语句: 从列表按照给定的索引而不是值来移除一个元素
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a

# --------------------------------------- 元组和序列 ------------------------------------------------
# 序列类型: list / tuple / range
# 1.1 元组tuple: Python的元组与列表类似，不同之处在于元组的元素不能修改;
#               元组使用小括号，列表使用方括号;
#               元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可.
tup = ('physics', 'chemistry', 1997, 2000)
tup = ()  # 空元组
tup = ('physics',)  # 元组中只包含一个元素时，需要在元素后面添加逗号

fruits = ('apple', 'banana', 'orange')
tupfruits = tup + fruits  # 元组不允许修改,但是可以连接组合

del tup  # 删除元组

# --------------------------------------- 集合 ------------------------------------------------

# 集合是由不重复元素组成的无序的集。它的基本用法包括成员检测和消除重复元素。集合对象也支持像 联合，交集，差集，对称差分等数学运算。
# {} 或 set() 函数可以用来创建集合。注意：要创建一个空集合你只能用 set() 而不能用 {}, 因为{}是创建一个空字典

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
a = set('abracadabra')  # 去除重复值

# --------------------------------------- 字典 ------------------------------------------------
# 字典在其他语言里可能会被叫做 联合内存 或 联合数组;
# 与以连续整数为索引的序列不同，字典是以 关键字 为索引的，关键字可以是任意不可变类型，通常是字符串或数字;
# 如果一个元组只包含字符串、数字或元组，那么这个元组也可以用作关键字。但如果元组直接或间接地包含了可变对象，那么它就不能用作关键字;
# 列表不能用作关键字，因为列表可以通过索引、切片或 append() 和 extend() 之类的方法来改变。

info = {'name': 'runoob', 'url': 'www.runoob.com', 'likes': 123}
print(list(info))  # list(d) 将返回包含该字典中所有键的列表

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])  # dict()构造函数可以直接从键值对序列里创建字典

# 1.1 修改字典
dict = {'Name': 'Runoob', 'Age': 8, 'Class': 'First'}
dict['Age'] = 8

# 1.2 删除字典元素
del dict['name']  # 删除键'name'
dict.clear()  # 清空字典
del dict  # 删除字典

# 1.3 字典的特性
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}

# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
dict = {['Name', ]: 'Runoob', 'Age': 7}

# 1.4 循环的技巧
# 当在字典中循环时，用 items() 方法可将关键字和对应的值同时取出
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key, value in knights.items():
    print(key, ':', value)

for key in knights:
    print(key)

# 当在字典中循环时，用 keys() 方法可将关键字取出
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key in knights.keys():
    print(key)

# 当在字典中循环时，用 values() 方法可将关键字取出
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for value in knights.values():
    print(value)

# 当在序列中循环时,用 enumerate() 函数可以将索引位置和其对应的值同时取出
for key, value in enumerate(['apple', 'banana', 'orange']):
    print(key, ':', value)

# 当同时在两个或更多序列中循环时，可以用 zip() 函数将其内元素一一匹配
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is you {0}? It is {1}.'.format(q, a))

# 当逆向循环一个序列时，先正向定位序列，然后调用 reversed() 函数
for i in reversed(range(1, 10, 2)):
    print(i)

# 如果要按某个指定顺序循环一个序列，可以用 sorted() 函数，它可以在不改动原序列的基础上返回一个新的排好序的序列
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# 对一个序列使用 set() 将去除重复的元素。 对一个序列使用 sorted() 加 set() 则是按排序后顺序循环遍历序列中唯一元素的一种惯用方式
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in set(basket):
    print(i)

# 在循环时修改列表内容，一般来说改为创建一个新列表是比较简单且安全的
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data =[]
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

# python在表达式内部赋值必须显式地使用 海象运算符 := 来完成,避免了想要在表达式中写==写成了=的问题
