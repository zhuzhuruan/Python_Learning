# -*- coding:utf-8 -*-

import pandas as pd

# data1 = pd.read_csv("./file/某招聘网站数据.csv", skiprows = lambda x : x !=0 and not x % 2 )
# data2 = pd.read_csv("./file/某招聘网站数据.csv", usecols = [0])
# # print(data2)
#
#
# data3 = pd.read_csv("./file/某招聘网站数据.csv", nrows=20, usecols=['positionId', 'positionName'])
# # print(data3)
# data3_iterator = data3.__iter__()      # 可迭代对象
# print(data3_iterator.__next__())       # 迭代器对象
# print(data3_iterator.__next__())       # 迭代器对象


data = pd.read_csv("./file/某招聘网站数据.csv")
print(data)

