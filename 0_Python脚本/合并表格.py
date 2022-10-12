import pandas as pd
import os
import openpyxl


def read_data(path, mode):
    """

    :param path:
    :param mode:
    :return:
    """
    data = None
    if mode == '1':
        data = pd.read_excel(path)
    elif mode == '2':
        data = pd.read_csv(path, encoding='utf-8', sep='\t')
    return data


def output_data(path, data):
    """
    输出txt
    """
    with open(path, 'a+', encoding='utf-8') as f:
        for line in data.values:
            f.write((str(line[0]) + '\t' + str(line[1]) + '\n'))


def concat_data(path_list):
    """
    合并表格
    :param path_list:
    :return:
    """
    list = []
    for path in path_list:
        data = read_data(path)
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
        file_name = f'待分拣数据_{i}.xlsx'
        df_sub.to_excel(file_name, engine='xlsxwriter')


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
        myNewSheet = myNewBook.active
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
    #  测试拆分一个excel到多个sheet
    # print(os.getcwd())
    # split_excel_to_sheet()

    path = r"C:\Users\caoyuanyuan\Desktop\项目文档\2-企业WiFi库\企业WiFi库精筛\待分拣数据\待分拣数据_1011\ssid_wait_check_1011.csv"
    # path_list = []
    # for file_path, dir_name, file_names in os.walk(path):
    #     for file in file_names:
    #         file_name = os.path.join(file_path, file)
    #         path_list.append(file_name)
    # df = concat_data(path_list)
    # df.to_excel(path)
    df = read_data(path, '2')
    # print(df.head())
    split_excel(df, 5)
