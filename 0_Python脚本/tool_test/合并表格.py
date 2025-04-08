import csv
import pandas as pd
import os
import openpyxl


def get_path_list(path):
    """
    多个文件合并时先获取文件列表
    :return:
    """
    path_list = []
    for file_path, dir_name, file_names in os.walk(path):
        for file in file_names:
            file_name = os.path.join(file_path, file)
            path_list.append(file_name)
    return path_list


def mixed_file(path, path_list):
    """
    合并多个txt文件
    :param path_list: 待合并的文件列表
    :return: 合并后的txt文件
    """
    content = ''
    # 循环读取文件内容
    for file in path_list:
        with open(file, 'r', encoding='utf-8') as f:
            content = content + f.read()
    # 保存文件
    with open(path + '\合并后的文件.txt', 'a', encoding='utf-8') as file:
        file.write(content)


def read_data(path, mode):
    data = None
    if mode == '1':
        data = pd.read_excel(path)
    elif mode == '2':
        data = pd.read_csv(path, encoding='utf-8', sep='\t', quoting=csv.QUOTE_NONE)
    return data


def output_data(path, data):
    with open(path, 'a+', encoding='utf-8') as f:
        for line in data.values:
            f.write((str(line[0]) + '\t' + str(line[1]) + '\n'))


def concat_data(path_list, mode):
    """
    合并表格
    :param path_list:
    :return:
    """
    list = []
    for path in path_list:
        file_name_type = os.path.basename(path)
        file_name = file_name_type.split('-')[0]
        data = read_data(path, mode)
        data['oiid'] = file_name
        list.append(data)
    merge_data = pd.concat(list, axis=0)
    # merge_distinct = merge_data.drop_duplicates(keep='first', inplace=False)
    # df = pd.DataFrame(merge_distinct)
    return merge_data


def split_excel(df, split_num):
    """
    拆分表格，输出多个文件
    :param df:
    :param split_num:
    :return:
    """
    total_row_count = df.shape[0]  # 100
    split_size = total_row_count // split_num  # 33
    if total_row_count % split_num != 0:
        split_size += 1  # 34

    # 按照索引开始拆分
    for i in range(0, split_num):  # 0,1,2
        begin = i * split_size
        end = begin + split_size
        df_sub = df.iloc[begin:end]  # [0,34],[34,68],[68,100]
        file_name = f'./file/test_{i}.csv'
        df_sub.to_csv(file_name)


def split_excel_to_sheet():
    # 读取“录取表.xlsx”文件
    myBook = openpyxl.load_workbook('file/录取表.xlsx')
    mySheet = myBook['录取表']
    # 按行获取录取表(mySheet)的单元格数据(myRange)
    myRange = list(mySheet.values)
    # 创建空白字典(myDict)
    myDict = {}
    # 从录取表(myRange)的第4行开始循环(到最后一行)
    for myRow in myRange[3:]:
        # 如果在字典(myDict)中存在某录取院校(myRow[0])，
        # 则直接在某录取院校(myRow[0])中添加考生([myRow])
        if myRow[0] in myDict.keys():
            myDict[myRow[0]] += [myRow]
        # 否则创建新录取院校
        else:
            myDict[myRow[0]] = [myRow]
    # 循环字典(myDict)的成员
    for myKey, myValue in myDict.items():
        # 创建新工作簿(myNewBook)
        myNewBook = openpyxl.Workbook()
        myNewSheet = myNewBook.actives
        # 在新工作表(myNewSheet)中添加表头(录取院校、专业、考生姓名、总分)
        myNewSheet.append(myRange[2])
        # 在新工作表(myNewSheet)中添加键名(录取院校)下的多个键值(考生)
        for myRow in myValue:
            myNewSheet.append(myRow)
        myNewSheet.title = myKey + '录取表'
        # 保存拆分之后(各个录取院校)的工作簿(myNewBook)，或者说保存各个Excel文件
        myPath = '结果表-' + myKey + '录取表.xlsx'
        myNewBook.save(myPath)


if __name__ == '__main__':
    # path = r'./file/test.csv'

    #  测试拆分一个excel到多个sheet
    # print(os.getcwd())
    # split_excel_to_sheet()

    # 精筛结果合并
    # df = concat_data(path_list, '2')
    # print(df.head())

    # 拆分表格
    # df = read_data(path, '2')
    # split_excel(df, 15)

    path_list = get_path_list(r'C:\Users\caoyuanyuan\Desktop\项目文档\GA项目\2-个案\个案-202411\易受骗人群\新建文件夹\新建文件夹')
    # path = r'C:\Users\caoyuanyuan\Desktop\项目文档\Python脚本\file\待合并文件'
    # mixed_file(path, path_list)
    merge_data = concat_data(path_list, '1')
    merge_data.to_excel(r'C:\Users\caoyuanyuan\Desktop\项目文档\GA项目\2-个案\个案-202406\个案-GA\郓城个案申请\郓城个案申请\合并.xlsx')
