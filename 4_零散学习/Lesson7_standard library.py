# --------------------------------------- 标准库 ------------------------------------------------

# 1.操作系统接口
import os
import urllib

os.getcwd()  # 返回当前的工作目录
os.chdir()  # 修改当前的工作目录
os.system('mkdir today')  # 执行系统命令 mkdir

dir(os)
help(os)

# 2.文件通配符
import glob  # glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:

glob.glob('*.py')

# 3.字符串正则匹配
import re

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# 4.数学
import math  # math模块为浮点运算提供了对底层C函数库的访问
import random  # random提供了生成随机数的工具

math.cos(math.pi / 4)
math.log(1024, 2)

random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)
random.random()
random.randrange(6)

# 5.访问互联网
# 有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
# for urllib.request import urlopen
# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')
#     if 'EST' in line or 'EDT' in line:
#         print(line)

# 5.日期和时间
# datetime模块为日期和时间处理同时提供了简单和复杂的方法，支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
from datetime import date

now = date.today()

# --------------------------------------- 虚拟环境和包 ------------------------------------------------
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
