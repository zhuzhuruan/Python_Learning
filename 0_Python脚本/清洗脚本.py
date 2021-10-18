# -*- coding: utf-8 -*-

import pandas as pd
import regex
import pymysql
import os

def read_data(path, sheet_name='Sheet1'):
    data = pd.read_excel(path, sheet_name=sheet_name, header=None)
    return data


def clean_data(data):
    row_list = []
    for i in data.index:
        for j in data.columns:
            if data.loc[i][j] == '施工单位':
                row_list.append(i)

    # print(row_list)

    company_lst = []
    for index in range(0, len(row_list)):
        # row_list[0]=2, row_list[1]=10, row_list[2]=19, row_list[3]=28, row_list[4]=37,
        if row_list[index] < row_list[-1]:
            print(row_list[index]+1, row_list[index+1])

            for i in range(row_list[index]+1, row_list[index+1]-2):
                for j in data.columns:
                    if j != 0 and data.loc[i][j] != '/' and j != data.columns.size - 1:
                        problem_type = data.loc[i][j]
                        date_range = data.loc[row_list[index]][data.columns.size - 1]
                        build_company = data.loc[row_list[index]][j]
                        road_name = data.loc[row_list[index] - 1][j].replace('（','(').replace('）',')')
                        district = data.loc[row_list[index] - 2][j]
                        if regex.search('(?<=\)).*',road_name):
                            build_type = regex.search('(?<=\)).*',road_name).group(0)
                        else:
                            build_type = None
                            print(road_name)
                        company_dict = {'date_range':date_range, 'build_company':build_company, 'build_type':build_type, 'district':district, 'road_name':road_name, 'problem_type':problem_type}
                        # print(company_dict)
                        company_lst.append(company_dict)
    return company_lst


def insert(data):
    conn = pymysql.connect(host="152.136.28.36", user="datauser", passwd="ZB_datauser", db="shjjw", charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    insert_sql = '''insert into zgzx_jkx_problem_2021(date_range, build_company, build_type, district, road_name, problem_type) 
                    values(%(date_range)s, %(build_company)s, %(build_type)s, %(district)s, %(road_name)s, %(problem_type)s)  
    '''

    cursor.executemany(insert_sql, data)
    conn.commit()

    cursor.close()
    conn.close()


def yuqing_data():
    data_lst = []
    file_names = os.listdir("D:/mydata/2-社情民意/2019")
    for file in file_names:
        path = os.path.join("D:\\mydata\\2-社情民意\\2019", file)
        data = pd.read_excel(path)
        data_lst.append(data)

    df = pd.concat(data_lst)
    # df.to_excel("D:\\mydata\\2-社情民意\\2019\\合并版本.xlsx")
    print(df.shape[0])



if __name__ == '__main__':
    # path = r'D:\mydata\16_综管中心第六版修改\测试0916.xlsx'
    # data = read_data(path)
    # result = clean_data(data)
    # insert(result)
    yuqing_data()