# -*- coding:utf-8 -*-
import os
from typing import List
from win32com import client as wc
import pdfplumber
import regex
import docx
import pandas as pd

regex_dict = {
    "I00101": {
        "class1_name": "设备侧滚",
        "class2_name": "设备侧滚过大",
        "keywords": "侧滚"
    },
    "I00201": {
        "class1_name": "设备倾角",
        "class2_name": "设备倾角过大",
        "keywords": "倾角"
    },
    "I00301": {
        "class1_name": "液压油箱温度",
        "class2_name": "液压油箱温度过高",
        "keywords": "液压油"
    },
    "I00401": {
        "class1_name": "齿轮油箱温度",
        "class2_name": "齿轮油箱温度过高",
        "keywords": "齿轮油"
    },
    "I00501": {
        "class1_name": "刀盘速度",
        "class2_name": "刀盘转速过快",
        "keywords": "刀盘转速"
    },
    "I00601": {
        "class1_name": "刀盘转矩",
        "class2_name": "刀盘转矩过大",
        "keywords": "刀盘转矩|扭矩"
    },
    "I00701": {
        "class1_name": "油缸推进压力",
        "class2_name": "油缸推进压力过大",
        "keywords": "油缸压力|油压"
    },
    "I00801": {
        "class1_name": "土压",
        "class2_name": "地层坍塌",
        "keywords": "坍塌|塌陷|塌方"
    },
    "I00802": {
        "class1_name": "土压",
        "class2_name": "地层突然变化",
        "keywords": "地层突变"
    },
    "I00803": {
        "class1_name": "土压",
        "class2_name": "压力传感器故障",
        "keywords": "压力传感器故障"
    },
    "I00901": {
        "class1_name": "推进速度",
        "class2_name": "推进速度过快",
        "keywords": "推进速度"
    },
    "I01001": {
        "class1_name": "总推进力",
        "class2_name": "地层坚实",
        "keywords": "推力"
    },
    "I01002": {
        "class1_name": "总推进力",
        "class2_name": "地层突然变化",
        "keywords": "地层突变"
    },
    "I01101": {
        "class1_name": "铰接油缸压力",
        "class2_name": "油压轻微异常",
        "keywords": "铰接油缸压力"
    },
    "I01102": {
        "class1_name": "铰接油缸压力",
        "class2_name": "油压中度异常",
        "keywords": "铰接油缸压力"
    }
}


def getfilename(file_data_path: str) -> List[str]:
    """
    获取文件名
    :param file_data_path: 文件夹路径
    :return: 文件路径列表
    """
    filename_list = []
    for file_path, dir_names, file_names in os.walk(file_data_path):  # 原始路径名、文件夹名、文件名
        for file in file_names:
            file_name = os.path.join(file_path, file)
            filename_list.append(file_name)
    return filename_list


def read_pdf(path: str) -> str:
    """
    读取pdf文本
    :param path: pdf文本路径
    :return: 文本字符串
    """
    long_text_list = []
    with pdfplumber.open(path) as pdf:  # 使用with语句打开pdf文件
        for page in pdf.pages:  # 使用for循环遍历每个pages
            text = page.extract_text()  # 提取文本
            if text is not None:
                long_text_list.append(text)
    long_text = '\n'.join(long_text_list)
    return long_text


def read_word(path: str) -> str:
    """
    读取word文件
    :param path: word文本路径
    :return: 文本字符串
    """
    long_text_list = []
    document = docx.Document(path)
    for para in document.paragraphs:
        long_text_list.append(para.text)
    long_text = '\n'.join(long_text_list)
    return long_text


def identify_keywords(content: str) -> List[str]:
    """
    识别关键词
    :param content: 识别的文本
    :return: 标签列表
    """
    tag = []
    for key in regex_dict.keys():
        if regex.search(regex_dict[key]['keywords'], content):
            tag.append(key)
    return tag


def file_identify_tag(filename: str) -> dict:
    """
    识别文件标签
    :param filename: 文件名
    :param long_text: 从文件中读取的文本字符串
    :return:字典：{file, tag}
    """
    try:
        if os.path.splitext(filename)[1] == '.pdf':
            long_text = read_pdf(filename)
            if long_text is None:
                print("{}是图片形式，无法读取".format(os.path.basename(filename)))
        elif os.path.splitext(filename)[1] == '.docx':
            long_text = read_word(filename)
        tag = identify_keywords(long_text)
        file_tag_dic = {'file_name': filename, 'tag': tag}
        return file_tag_dic
    except:
        print("{}.文件格式有问题".format(filename))


def doSaveAas(doc_path: str):
    """
    把doc文件转换成docx文件
    :param doc_path: 文件路径
    :return:
    """
    word = wc.Dispatch('Word.Application')  # 打开word应用程序
    doc = word.Documents.Open(doc_path)  # 目标路径下的文件
    doc.SaveAs("{}x".format(doc_path), 12)  # 转化后路径下的文件
    doc.Close()
    word.Quit()


def get_tag_process(filename_list: List[str]) -> List[dict]:
    """
    获取标签结果
    :param filename_list: 文件名列表
    :return: 标签结果列表
    """
    file_tag_list = []
    # 识别标签
    # for file in filename_list:
    for index, file in enumerate(filename_list):
        if round((index + 1) * 100 / len(filename_list)) % 10 == 0:         # 进度条
            print(str(str(round((index + 1) * 100 / len(filename_list))) + '%').center(50, '='))

        if os.path.splitext(file)[1] == '.pdf' or os.path.splitext(file)[1] == '.docx':
            file_tag_dic = file_identify_tag(file)
            file_tag_list.append(file_tag_dic)
        elif os.path.splitext(file)[1] == '.doc':
            try:
                doSaveAas(file)
                file_tag_dic = file_identify_tag(os.path.splitext(file)[0] + '.docx')
                file_tag_list.append(file_tag_dic)
            except:
                print("{}.文件格式有问题".format(file))

    return file_tag_list


def insert_excel(data_list: List[dict], out_path: str):
    """
    结果写出
    :param data_list: 列表结果
    :param out_path: 输出文件路径
    :return:
    """
    df = pd.DataFrame(data_list, columns=['file_name', 'tag'])
    df.to_excel(out_path)


def main_process(input_path: str, output_path: str):
    """
    主过程
    :param input_path: 读取文件夹路径
    :param output_path: 输出文件路径
    :return:
    """
    filename_list = getfilename(input_path)
    file_tag_list = get_tag_process(filename_list)
    insert_excel(file_tag_list, output_path)


if __name__ == "__main__":
    input_path = r"D:\mydata\15_盾构\05 专项方案\05 专项方案"
    output_path = r"D:\mydata\15_盾构\05 专项方案\05_专项方案.xlsx"
    # input_path = input("请输入您的读取文件夹路径<D:\\input_path>: ")
    # output_path = input("请输入您的输出文件路径<D:\\output_path\\file.xlsx>: ")
    main_process(input_path, output_path)
