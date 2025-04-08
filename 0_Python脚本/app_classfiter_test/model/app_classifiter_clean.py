# -*- coding: utf-8 -*-
# @Time : 2024/11/2910:32
# @Author : cyy
# @File : app_classifiter_clean.py
# @desc :


import pandas as pd
import re
import jieba
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import itertools

# 加载自定义词典文件
jieba.load_userdict('../config/not_split_word.txt')


def read_data(path, file_name):
    """
    读取分拣数据
    :param path:
    :return:
    """
    data = pd.read_excel(f'{path}/{file_name}.xlsx')[['apppkg', 'appname', 'cate']]
    return data


def remove_special_characters(text):
    """
    将apppkg_name中的特殊字符处理为空字符串
    :param text:
    :return:
    """
    pattern = '(?:v|vip)_?[0-9]+(?:\.[0-9]+)?$|[^\u4e00-\u9fa5a-zA-Z0-9]'
    clean_text = re.sub(pattern, ' ', re.sub('\n\t', '', text)).strip()
    chinese_part = ''.join([s.lower() for s in re.findall('[\u4e00-\u9fa5]', clean_text)]).strip()
    else_part = ''.join([s.lower() for s in re.findall('[^\u4e00-\u9fa5]', clean_text)]).strip()
    return chinese_part.lower() + ' ' + else_part.lower()


def tokenize_english_text(text):
    """
    对apppkg分词,并移除特定域名
    :param text:
    :return:
    """
    # 加载停用词
    with open('../config/stop_data.json', 'r', encoding='utf-8') as f:
        stop_content = json.load(f)
        gTLDs = list(stop_content['gTLDs'].keys())
        class_example = list(stop_content['class_example'].keys())
        model_example = stop_content['model_example']['stop_word']
        stop_words_list = gTLDs + class_example + model_example
    # 分词并去除停用词
    text = re.sub('[^a-zA-Z0-9\.]|_', '', text)
    text_list = text.lower().split('.')
    text_result = []
    for word in text_list:
        if not (word in stop_words_list or len(word) == 1):
            text_result.append(word)
    return text_result


def tokenize_text(content):
    """
    对apppkg_name进行分词
    :param text:
    :return:
    """
    content_cut = []
    if re.search('[\u4e00-\u9fa5]', content):
        content_s = jieba.lcut(remove_special_characters(content))
    else:
        content_s = remove_special_characters(content).split(' ')
    for current_segment in content_s:
        if current_segment != '\r\n' and len(current_segment) >= 1 and current_segment != ' ':
            if not (re.search('^[0-9a-zA-Z]+$', current_segment) and len(current_segment) == 1):
                content_cut.append(current_segment.strip().lower())
    return content_cut


def tfidf_extractor(corpus, ngram_range=(1, 1)):
    """
    获取tf-idf值
    :param corpus:
    :param ngram_range:
    :return:
    """
    vectorizer = TfidfVectorizer(min_df=1, norm='l2', smooth_idf=True, use_idf=True, ngram_range=ngram_range)
    features = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names()
    return features, feature_names


def data_preprocess(data):
    """
    对apppkg和apppkg_name进行清洗
    :param data:
    :return:
    """
    # 类型转换成string
    data['apppkg'] = data['apppkg'].astype('string')
    data['appname'] = data['appname'].astype('string')
    # 空值填充
    data['apppkg'].fillna('', inplace=True)
    data['appname'].fillna('', inplace=True)
    # 清洗appname
    data['apppkg_clean'] = data['apppkg'].apply(lambda apppkg: tokenize_english_text(apppkg))
    data['appname_clean'] = data['appname'].apply(lambda appname: tokenize_text(appname))
    # 汇总
    data['word_all_clean'] = data.apply(lambda row: row['apppkg_clean'] + row['appname_clean'], axis=1)
    return data


if __name__ == '__main__':
    path = '../dataset'
    file_name = 'file_data'
    data = read_data(path, file_name)
    data_clean = data_preprocess(data)
    data.to_excel(r'../dataset/result.xlsx')

    # 将一列数据转为list
    # word_all_clean = data['word_all_clean'].values.tolist()
    # flat_list = list(itertools.chain(*word_all_clean))
    # cutWords_list = ' '.join([word for word in flat_list if word != '' and word != ' '])
    # with open('../config/cutWords_list.txt', 'w') as f:
    #     f.write(cutWords_list)

    word_all_clean = data['word_all_clean'].values.tolist()
    with open('../config/cutWords_list.txt', 'w', encoding='utf-8') as file:
        # 遍历列表中的每个元素
        for word_list in word_all_clean:
            cutWords_list = ' '.join([word for word in word_list if word != '' and word != ' '])
            # 将元素写入文件，并添加换行符
            file.write(cutWords_list + '\n')

    # 创建一个字典，其中键是列名，值是列的数据
    # data = {
    #     'text': ['你好啊我在北京见过你', '玛丽真是一个漂亮的女孩'],
    #     'Age': [25, 30],
    # }

    # # 使用字典创建 DataFrame
    # train_data = pd.DataFrame(data)

    #
    # # 构造数据集迭代器
    # def coustom_data_iter(texts, labels):
    #     for x, y in zip(texts, labels):
    #         yield x, y
    #
    #
    # train_iter = coustom_data_iter(train_data['text'].values[:], train_data['Age'].values[:])
    # print(next(train_iter))
    # print(next(iter(train_iter)))
