# -*- coding:utf-8 -*-
import time

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series
import json
import regex

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

#
# df = pd.read_csv("./file/某招聘网站数据.csv")
#
# # df = df.head(10)
#
# # 筛选行
# df_row1 = df[1:5]           # 1,2,3,4
#
# df_row2 = df.loc[1:5]       # 1,2,3,4,5
# df_row3 = df.loc[[1,3,5]]   # 1,3,5
#
# df_row4 = df.iloc[0:5]      # 0,1,2,3,4
# df_row5 = df.iloc[[0,3,5]]
#
# # 筛选列
# df_col1 = df['positionId']          # positionId
# df_col2 = df[['positionId','positionName', 'companyId']]         # positionId,positionName,aggregatePositionIds
#
# df_col3 = df.loc[:, "positionId":"companyId"]
# df_col4 = df.loc[:, ["positionId","companyId"]]
#
# df_col5 = df.iloc[:, 0:3]
# df_col6= df.iloc[:, [0, 3, 6]]
#
# # print(df_row5)
#

# s = Series(np.random.randn(10))
# print(s.sort_values())
# plt.hist(s)
# s.plot(kind='kde')
# plt.show()


# with open('test1.json', 'rt', encoding='utf-8') as f:
#     lst = json.load(f)
#     print(lst)

# ages = np.array([1,5,10,40,36,12,58,62,77,89,100,18,20,25,30,32]) #年龄数据
# print(ages)
# res = pd.cut(ages, [0,5,20,30,50,100],retbins=True)
# print(res)

r = "\d+\.?\d+[/*~_－]?[/-]?\d+\.?\d+mm"
import re

RE_RGB_PATTERN = re.compile(r"\d+\.?\d{0,3}(?:mm)?[/*~_－]?[/-]?\d{0,3}(?:\.\d+)?mm", re.IGNORECASE)
RE_RGB_PATTERN1 = re.compile(r"\d+(?:\.\d+)?(?:mm)?", re.IGNORECASE)


def test():
    content = ["6mm", "0.5mm/12mm", "0.5*0.38mm", "0.5-0.38mm", "0.5－0.38mm", "0.5/0.38mm", "28-40mm", "26.65mm",
               "0.5mm/0.38mm", "28-40mm", "0.5*0.38mm", "0.5-0.38mm", "0.5/0.38mm", "0.5－0.38mm", "28mm",
               "0.5mm/0.38mm", "0.05mm", "0.28mm", "K35/0.5mm"]
    for i in content:
        _nips = RE_RGB_PATTERN.findall(i)
        print(i, _nips)
        # for j in _nips:
        #     if set(list("*~_－-")) & set(list(j)):
        #         print('----')
        #     else:
        #         v = RE_RGB_PATTERN1.findall(j)
        #         print(j, v)


def test2():
    page_dict = {6: 700, 2: 700, 4: 400, 8: 400, 10: 100}
    value_lst = [value for value in page_dict.values()]
    same_value = list(set([i for i in value_lst if value_lst.count(i) > 1]))

    for i in same_value:
        a = []
        for key, value in list(page_dict.items()):
            if value == i:
                a.append(key)
                del page_dict[key]
        page_dict[sum(a)] = i

    print(page_dict)


def test3():
    # mata = {'name':"cyy"}
    # if not mata:
    #     print("OK")
    #
    # x = {"a", "b", "c"}
    # print("+".join(x))
    #
    # PATTERN1 = re.compile(r"硒鼓|鼓架|芯片|粉[盒筒]|粉盒|[碳墨]粉(?![盒筒])|感光鼓(?:组件)?")
    # res = PATTERN1.findall("感光鼓")
    # print(res)

    # if res:
    #     powder_box = [item for item in res if re.search('[粉墨][盒筒瓶]', item)]
    #     powder = [item for item in res if re.search('[碳墨]粉(?![盒筒瓶])', item)]
    #     if powder_box and powder:
    #         for i in powder:
    #             res.remove(i)
    #     print(res)

    # price=0
    # if price:
    #     print("OKKK")

    # data = pd.read_excel("D:/mydata/17_价格监测/硒鼓品类测试样例.xlsx", sheet_name=3)
    # data["models"] = None
    # for i in data.index:
    #     if i == 4:
    #         s = data.loc[i]['information']
    #         if isinstance(s, str):
    #             print(s)
    #             params_mapping = s.replace("\\", "").replace('""', '"').strip('"')
    #             print(params_mapping)
    #
    #             params_mapping = json.loads(params_mapping)
    #             print(type(params_mapping))

    s = '{"类型": "通用耗材", "规格": "超值装/大容量", "颜色": "彩色", "包装清单": "\"W9100MC黑色粉盒*1W9101MC蓝色粉盒*1W9102MC黄色粉盒*1W9103MC红色粉盒*1\"", "商品产地": "中国大陆", "商品名称": "彩格W9100MC", "商品毛重": "3.2kg", "商品编号": "100010813041"}'
    s = s.replace("\\", "").strip('"')
    params_mapping = json.loads(s)
    print(type(params_mapping))


def data_process(start, end):
    ...


def run(start_cnt, run_max):
    start_pk = start_cnt
    end_pk = run_max

    while start_cnt < run_max:
        run_limit = min(500, run_max - start_cnt)
        print("process:[%s,%s] run from %s and %s" % (start_pk, end_pk, start_cnt, start_cnt + run_limit - 1))
        data_process(start_cnt, start_cnt + run_limit - 1)
        start_cnt += run_limit
    print("item_category process end")


def get_time():
    print(time.time())


def get_strf_time():
    start = time.localtime()
    print(time.strftime('%Y-%m-%d %H:%M:%S', start))


def test_run(**kwargs):
    # get_time(1)
    # get_strf_time = kwargs.get("get_strf_time")
    # get_strf_time()
    #
    print(kwargs)
    for value in kwargs.values():
        value()


# transNum

def transNum(num):
    han = "零一二三四五六七八九"
    for i in range(len(num)):
        num_split = int(num[i])
        print(han[num_split], end='')


def test4(flags):
    if flags == 4:
        pattern_model = re.compile(r'([a-zA-Z][a-zA-Z0-9\-\－\s]*[0-9]+[a-zA-Z0-9\－\-\s]*[a-zA-Z0-9]*)')
    else:
        pattern_model = re.compile(r'([a-zA-Z0-9][a-zA-Z0-9\-\－]*[0-9]+[a-zA-Z0-9\－\-]*[a-zA-Z0-9]*)')

    content = '8555ES【19mm】(40只/筒)'
    res = pattern_model.findall(content)
    # res = sorted(res, key = lambda i:len(i),reverse=True)
    print(res)
    str = '-200'
    print(re.findall(r'品牌|商品名称', str))

    x = re.sub(r'[0-9]+[mMcC][Mm]|[\-\－]', '', str)
    print(x)


def test5():
    pattern = re.compile(r'[0-9]+[\u4e00-\u9fa5()（）]{0,4}[\-\－][0-9]+')
    x = re.findall(pattern, '1张(含)-500张含')
    print(x)


if __name__ == '__main__':
    # test_run(get_time=get_time, get_strf_time=get_strf_time)
    # num = input("请输入阿拉伯数字：")
    # transNum(num)
    # test4(6)

    test5()
