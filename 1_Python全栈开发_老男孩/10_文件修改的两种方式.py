# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------文件-------------------------------------------------
方式一：文本编辑器采用的方式
file = 'practice_file\\文件的使用.txt'
with open(file, 'rt', encoding='utf-8') as f:
    res = f.read()
    res_change = res.replace('赵二', '钱五')
with open(file, 'wt', encoding='utf-8') as f:
    f.write(res_change)


方式二：
import os
file_r = 'practice_file\\文件的使用.txt'
file_w = 'practice_file\\.文件的使用.swap.txt'
with open(file_r, 'rt', encoding='utf-8') as f, open(file_w, 'wt', encoding='utf-8') as f1:
    for line in f:
        f1.write(line.replace('赵一', '赵六'))
os.remove(file_r)
os.rename(file_w, file_r)

"""

