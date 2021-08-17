# --------------------------------------- 格式化输出 ------------------------------------------------
# 1.输出格式美化: 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值;
#               如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
import collections
import math

s = 'Hello World!'
str(s)  # str()：函数返回一个用户易读的表达形式
repr(s)  # repr()： 产生一个解释器易读的表达形式。

hello = 'hello, runoob\nhello runoob'
hellos = repr(hello)  # repr() 函数可以转义字符串中的特殊字符

print(hello)
print(hellos)

# 2.格式化字符串字面值(f' \ F'): （常简称为 f-字符串）能让你在字符串前加上 f 和 F 并将表达式写成 {expression} 来在字符串中包含 Python 表达式的值。
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'

print(math.pi)
print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

# 3.字符串str.format()方法: 花括号和其中的字符（称为格式字段）将替换为传递给 str.format() 方法的对象。花括号中的数字可用来表示传递给 str.format()方法的对象的位置
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))  # 使用关键字参数
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))  # 位置参数和关键字参数同时使用

print('常量PI的值近似为: {}.'.format(math.pi))
print('常量PI的值近似为: {!r}.'.format(math.pi))  # !r → repr()
print('常量PI的值近似为: {!a}.'.format(math.pi))  # !a → acsii()
print('常量PI的值近似为: {!s}.'.format(math.pi))  # !s → str()

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# --------------------------------------- 读写文件 ------------------------------------------------
# open(filename, mode): filename：包含了你要访问的文件名称的字符串值;
#                       mode：决定了打开文件的模式：只读，写入，追加等。
# 'r':  以只读方式打开文件,表示文件只能读取。
# 'w':  打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# 'a':  打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# 'r+': 打开一个文件用于读写。
# mode 参数是可选的；省略时默认为 'r'。

workfiles = 'D:/mydata/cyy/CYY_Projects/foo.txt'

# 1.write(string): 会把字符串的内容写入文件中,并返回写入的字符数;在写入其他类型的对象之前，需要先把它们转化为字符串或者字节对象
with open(workfiles, "w") as f:
    f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
f.closed

with open(workfiles, "a") as f:
    f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
f.closed

# 2.文件对象的方法:
# f.read(): 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
#           size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
with open(workfiles, "r", encoding='utf-8') as f:
    data = f.read()
f.closed

# readline() : 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
#                每次读出一行内容，所以，读取时占用内存小，比较适合大文件，该方法返回一个字符串对象。
with open(workfiles, "r", encoding='utf-8') as f:
    data = f.readline()
f.closed

# readlines(): 读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存。
with open(workfiles, "r", encoding='utf-8') as f:
    data = f.readlines()
f.closed

with open(workfiles, "r", encoding='utf-8') as f:
    for line in f:
        print(line)
f.closed

# --------------------------------------- json ------------------------------------------------
# 3.使用json保存结构化数据
# load() & loads() :这两个方法中都是把其他类型的对象转为Python对象(列表，元组，字典，自定义的类等),当然不包括Python的字符串类型
# 不同点: load操作的是文件流; loads()操作的是字符串
# 相同点: 除要转换的对象类型不同外,其他参数都一样,最终都是转换成python对象

# json.loads：用于解码 JSON 数据。该函数返回 Python 字段的数据类型(列表、字典等)
# json.dumps：用于将 Python 对象编码成 JSON 字符串

# loads： 是将string转换为dict
# dumps： 是将dict转换为string
# load： 是将里json格式字符串转化为dict，读取文件
# dump： 是将dict类型转换为json格式字符串，存入文件

import json

s = '{"name": "wade", "age": 54, "gender": "man"}'
s0 = json.loads(s)  # 把字符串形式的s转换成python的字典类型
s1 = json.dumps(s0)  # 把字典形式的s0转换成json字符串

s = '{"name": "wade", "age": 54, "gender": "man"}'
if __name__ == '__main__':
    print("json.loads将字符串转为Python对象: type(json.loads(s)) = {}".format(type(json.loads(s))))
    print("json.loads将字符串转为Python对象: json.loads(s) = {}".format(json.loads(s)))

with open('D:/mydata/cyy/CYY_Projects/demo.json', 'r', encoding='utf-8') as demo:
    s1 = json.load(demo)

with open('D:/mydata/cyy/CYY_Projects/demo1.json', 'r', encoding='utf-8') as demo:
    s2 = json.load(demo)

# json.loads默认将JSON中的对象数据转化为Dictionary类型, object_hook参数可以用来改变构造出的对象.
# object_hook接受一个函数, 这个函数的输入参数为JSON中对象数据转化出的Dictionary对象, 其返回值则为自定义的对象
# 很多人认为python中的字典是无序的，因为它是按照hash来存储的，但是python中有个模块collections(英文，收集、集合)，里面自带了一个子类
# OrderedDict，实现了对字典对象中元素的排序

