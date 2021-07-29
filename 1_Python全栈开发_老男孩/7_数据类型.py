# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------整型int-------------------------------------------------
一、十进制转换成其他进制
1、十进制转二进制：bin(x)
2、十进制转八进制：oct(x)
3、十进制转十六进制：hex(x)

二、其他进制转换为二进制
1、int(x , 进制)


-------------------------------------------------字符串类型str()-------------------------------------------------
一、内置方法
1、字符串反转
    str[::-1]

2、strip(): 去除字符串两边的字符
    str.strip()

3、isdigit()、isnumeric()
（1）判断字符串是否由纯数字组成
（2)区别：isdigit(): 只能识别阿拉伯数字
        isnumeric(): 可以识别阿拉伯数字、中文数字、罗马数字


 num1 = 4 ; num2 = '四' ; num3 = 'Ⅳ'
 print(num1.isdigit()) ; print(num2.isdigit()) ; print(num3.isdigit())
 print(num1.isnumeric()) ; print(num2.isnumeric()) ; print(num3.isnumeric())

4、find()、index()、rfind()、rindex()
（1）查找子字符串在原始字符串中的起始位置（索引）
（2）区别：当子字符串在原字符串中找不到时，find()返回-1，index()报错

5、count(): 子字符串在原字符串中出现的次数

6、center()、ljust()、rjust()、zfill()、expandtabs()
（1）控制字符串的输出格式
（2）str.center(): 居中填充
    str.ljust()、str.rjust(): 向左、向右填充
    str.zfill(): 用0填充
（3）expandtabs()：设定制表符代表的空格数
    "Hello\tWorld!".expandtabs(4)

7、capitalize()、swapcase()、title()
（1）str.capitalize(): 字符串首字母大写
（2）str.swapcase(): 字符串字母大小写反转
（3）str.title(): 字符串中的每个单词首字母大写


-------------------------------------------------列表类型list()-------------------------------------------------
一、内置方法
1、append()、insert()、extend(): 列表添加值

2、del()、pop()、remove(): 列表删除值
（1）del(): 指定删除的索引，没有返回值
（2）pop(): 指定删除的索引，不指定则从结尾开始删，有返回值，返回值是列表中被删除的元素
（3）remove(): 根据元素删除，返回None

3、其他方法：count()、index()、clear()、reverse()、sort(key=, reverse=False)


-------------------------------------------------队列和堆栈-------------------------------------------------
1、队列：First In First Out(FIFO),先进先出
       # 模拟入队操作
       l = []
       l.append('First')
       l.append('Second')
       l.append('Third')
       print(l)
       # 模拟出队操作
       print(l.pop(0))
       print(l.pop(0))
       print(l.pop(0))

2、堆栈：Last In First Out(LiFO),后进先出
       # 模拟入栈操作
       l = []
       l.append('First')
       l.append('Second')
       l.append('Third')
       print(l)
       # 模拟出栈操作
       print(l.pop())
       print(l.pop())
       print(l.pop())


-------------------------------------------------元组tuple()-------------------------------------------------
注意：如果元组中只包含一个值，一定要加逗号，例如t = (10,)


-------------------------------------------------字典dict()-------------------------------------------------
一、数据类型转换
1、列表形式转字典
    l = [
        ['name', 'alex'], ['age', 15], ['gender', '男']
    ]
    d = dict(l)
    print(d)

2、快速初始化字典
    l = ['name', 'age', 'gender']
    d = {}.fromkeys(l, None)    # 设定初始值
    print(d)

二、内置方法
1、删除：del()、pop()、popitem()
（1）del(): 按照key删除，无返回值
（2）pop(): 按照key删除，返回被删除的key对应的value值
（3）popitem(): 随机删除，返回被删除的键值对元组(key, value)

2、更新字典：update()
    d = {'name': 'alex'}
    d.update({'age': 18, 'gender': '男'})
    d.update({'age': 18, 'gender': '男', 'name': 'Mary'})

2、get(): 按照key取值，如果没有对应的key,返回设定的值
        d = {'name': 'alex'}
        d.get('age', -1)

3、setdefault(): 判断key是否在字典中，如果有则pass,如果没有则把key和value添加进字典,有返回值，返回值是key对应的value
        d = {'name': 'alex'}
        d.setdefault(name, Mary)
        d.setdefault(age, 18)


-------------------------------------------------集合set()-------------------------------------------------
一、关系运算
1、交：&、intersection()
2、差：-、difference()
3、并：|、union()
4、补：^、symmetric_difference()
5、父子集：>/<、issuperset()/issubset()

二、去重功能
1、局限性：
（1）只能针对不可变类型去重
        print(set([1, 2, 3, ['a', 'b', 'b', 'c']]))
（2）无法保证原来的顺序

三、内置函数
1、删除: discard()、remove()
2、更新: update()



"""
