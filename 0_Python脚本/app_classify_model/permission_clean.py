# -*- coding: utf-8 -*-
# @Time : 2023/7/2411:07
# @Author : cyy
# @File : permission_clean.py
# @desc :

import json
import pandas as pd
import re
import os
from white_sample_deal import change_permission_output

pattern = re.compile('(?<=permission\\.).*')


def read_data(path):
    df = pd.read_csv(path, encoding='utf-8')
    return df


def read_json(in_path):
    """
    解析json文件,增加涉炸样本
    :param path:
    :return:
    """
    data_list = []
    for file_path, dir_name, file_names in os.walk(in_path):
        for file in file_names:
            file_name = os.path.join(file_path, file)
            with open(file_name, 'r', encoding='utf-8') as f:
                json_file = json.load(f)
                data_list.append(json_file)
    df = pd.DataFrame(data_list)
    df_res = df.loc[:, ['ApkPackage', 'APP名称', 'APK大小', 'MD5码', 'SDK信息', 'AndroidManifest.xml中的权限与权限说明']]
    df_res.rename(columns={'ApkPackage': 'pkg', 'APP名称': 'appname', 'APK大小': 'size', 'MD5码': 'md5', 'SDK信息': 'SDKS',
                           'AndroidManifest.xml中的权限与权限说明': 'permission'}, inplace=True)
    return df_res


def split_list_data(word_list):
    """
    将列表中的元素拆分并清洗
    :return:
    """
    if isinstance(word_list, str):
        word_list = eval(word_list)
    res_list = []
    permission_list = []
    if isinstance(word_list, list) and len(word_list) > 0:
        for word in word_list:
            # 针对json文件中[权限 权限说明]
            if re.search(r'[^\u4e00-\u9fa5]+ .*', word):
                keyword = word.split(' ')[0]
                description = ''.join(word.split(' ')[1:])
            else:
                # 标准格式中[权限]
                keyword = word
                description = ''
            if re.search(pattern, keyword):
                word_clean = re.search(pattern, keyword).group()
                res_list.append(word_clean)
                permission_list.append({'permission': word_clean, 'description': description})
        res_list = list(set(res_list))
    return res_list, permission_list


def count_num(list1, list2):
    for word in list1:
        if word in list2:
            return 1
    return 0


def get_permission_compare(df):
    """
    获取所有样本中的权限，对比权限的唯一性
    :return:
    """
    res = []
    permission_get = set(sum(df.permission_keyword.tolist(), []))
    for i in permission_get:
        permission_dict = {}
        for j in df.index:
            permission_list = df.loc[j, 'permission_keyword']
            app_type = df.loc[j, 'app_type']
            if i in permission_list:
                permission_dict[app_type] = permission_dict.get(app_type, 0) + 1
        res.append([i, permission_dict, len(permission_dict)])
    return res


def main(df, out_path1, out_path2, out_path3):
    # 获取清洗后的权限关键字
    list_of_tuples = df['permission'].apply(lambda x: split_list_data(x)).to_list()
    df[['permission_keyword', 'permission_list']] = pd.DataFrame(list_of_tuples, index=df.index)
    df['keyword_length'] = df['permission_keyword'].apply(lambda x: len(x))
    df.to_excel(out_path1)

    # 获取权限及其说明
    permission_desc = change_permission_output(df)
    permission_desc.to_excel(out_path3)

    # 获取权限在不同类型的数量
    res = get_permission_compare(df)
    permission_keyword = pd.DataFrame(res, columns=['permission_keyword', 'app_type', 'type_num'])
    permission_keyword.to_excel(out_path2)


if __name__ == '__main__':
    base_path = r'C:\Users\caoyuanyuan\Desktop\项目文档\GA项目\3-模型'
    in_file = 'all_data.csv'
    out_file1 = 'permission_res.xlsx'
    out_file2 = 'permission_num.xlsx'
    out_file3 = 'permission_desc.xlsx'

    in_path = os.path.join(base_path, in_file)
    out_path1 = os.path.join(base_path, out_file1)
    out_path2 = os.path.join(base_path, out_file2)
    out_path3 = os.path.join(base_path, out_file3)

    # 解析json文件
    # out_file3 = 'json_res.xlsx'
    # out_path3 = os.path.join(base_path, out_file3)
    # json_path = r'C:\Users\caoyuanyuan\Desktop\项目文档\GA项目\3-模型\已解析数据'
    # df = read_json(json_path)
    # main(df, os.path.join(base_path, f'json_permission.xlsx'))

    # 调用主函数
    # df = read_data(in_path)
    # main(df, out_path1, out_path2, out_path3)

    df = pd.read_excel(r'C:\Users\caoyuanyuan\Desktop\项目文档\GA项目\3-模型\permission_res.xlsx')
    print(df.head())
    df = df[df['app_type'] == 'json'].loc[:, ['permission_list']]
    print(df.head())
    df['permission_list'] = df['permission_list'].apply(lambda x: eval(x))
    x = sum(df['permission_list'].tolist(), [])
    print(x)
    permission_desc = pd.DataFrame(x)
    permission_desc.to_excel(out_path3)


