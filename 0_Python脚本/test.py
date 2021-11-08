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


df = pd.read_csv("./file/某招聘网站数据.csv")

# df = df.head(10)

# 筛选行
df_row1 = df[1:5]           # 1,2,3,4

df_row2 = df.loc[1:5]       # 1,2,3,4,5
df_row3 = df.loc[[1,3,5]]   # 1,3,5

df_row4 = df.iloc[0:5]      # 0,1,2,3,4
df_row5 = df.iloc[[0,3,5]]

# 筛选列
df_col1 = df['positionId']          # positionId
df_col2 = df[['positionId','positionName', 'companyId']]         # positionId,positionName,aggregatePositionIds

df_col3 = df.loc[:, "positionId":"companyId"]
df_col4 = df.loc[:, ["positionId","companyId"]]

df_col5 = df.iloc[:, 0:3]
df_col6= df.iloc[:, [0, 3, 6]]

# print(df_row5)

