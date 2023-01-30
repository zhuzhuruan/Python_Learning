# -*- coding: utf-8 -*-
# @Time : 2022/10/2510:52
# @Author : cyy
# @File : NLP分词工具.py
# @desc :


import companynameparser
import pandas as pd
import re
import time
import os


def read_data(path):
    df = pd.read_csv(path)
    return df


def readPart(filePath, size=1024, encoding="utf-8"):
    """
    使用迭代器读取海量数据
    :param filePath:
    :param size:
    :param encoding:
    :return:
    """
    with open(filePath, "r", encoding=encoding) as f:
        while True:
            part = f.read(size)
            if part:
                yield part
            else:
                return None


def read_line_part(filePath, file_name, size=50000):
    """
    # 采用文件句柄的方式
    :return:
    """
    global part_list
    file = os.path.join(filePath, file_name)
    with open(file, 'rt', encoding='utf-8') as f:
        count = 1
        part_list = []
        print("process begin start".center(100, '-'))
        for line in f:
            start = time.time()
            line = line.replace('\n', '')
            if count % size == 0 and count > 0:
                data = pd.DataFrame(part_list, columns=['company_name'])
                # 将公司名分词
                df = split_company(data)
                # 每50w输出一次
                df.to_csv(os.path.join(filePath, f'{out_put_name}_{count}.txt'), index=False, header=False, sep='\t')
                # 打印代码进度
                end = time.time()
                print(f"process have output: {count - size} between {count}, time: {end - start}s")
                # 将列表清空，生成新一轮的数据
                part_list = [line]
                count += 1
            else:
                part_list.append(line)
                count += 1
        # 剩余的部分
        data = pd.DataFrame(part_list, columns=['company_name'])
        df = split_company(data)
        df.to_csv(os.path.join(filePath, f'{out_put_name}_{count}.txt'), index=False, header=False, sep='\t')


def clean_name(name):
    name_clean = re.sub('[^\u4e00-\u9fa5]', '', name)
    return name_clean


def companynameparser_func(name):
    if name is not None:
        name_clean = clean_name(name)
        split_name = companynameparser.parse(name_clean)
        split_name['company_name'] = name
        # 如果brand或trade多个，并且由逗号分隔，则将其分裂并推到下一列
        for key, value in split_name.items():
            if ',' in value and key == 'brand':
                split_name[key] = value.split(',')[0]
                split_name['suffix'] = split_name['trade'] + "," + split_name['suffix']
                split_name['trade'] = value.split(',')[1]
            elif ',' in value and key == 'trade':
                split_name[key] = value.split(',')[0]
                split_name['suffix'] = value.split(',')[1] + "," + split_name['suffix']
        # 添加brand+trade, place+brand
        split_name['brand_trade'] = split_name['brand'] + split_name['trade']
        split_name['place_brand'] = split_name['place'].split(',')[0] + split_name['brand']
        del split_name['symbol']
        return split_name
    else:
        return None


def split_company(df):
    df['split_name'] = df['company_name'].apply(lambda x: companynameparser_func(x))
    column_list = df['split_name'].values.tolist()
    split_data = pd.DataFrame(column_list)

    # 更改列的顺序
    cols = split_data.columns.tolist()
    cols = cols[4:5] + cols[:4] + cols[5:]
    sort_data = split_data[cols]
    return sort_data


if __name__ == '__main__':
    filePath = './file/'
    file_name = 'test.txt'
    out_put_name = file_name.split('.')[0]

    # 读取少量数据
    # df = read_data(path)
    # split_data = split_company(df)
    # split_data.to_csv(f'./file/{file_name}.csv', index=False)

    # 单个测试
    # name = '侯马经济恒升商贸有限公司'
    # print(companynameparser_func(name))

    # 海量数据的读取(采用迭代器的方式)
    # size = 10240  # 每次读取指定大小的内容到内存
    # i = 0
    # for part in readPart(filePath, size, encoding='utf-8'):
    #     data = pd.DataFrame(part.split("\n"), columns=['company_name'])
    #     data.to_csv(f'./file/{file_name}_{i}.csv')
    #     i += 1

    # 海量数据的读取(采用文件句柄的方式)
    read_line_part(filePath, file_name, size=500000)
