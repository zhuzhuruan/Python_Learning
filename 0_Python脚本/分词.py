# -*- coding: utf-8 -*-
# @Time : 2022/6/1415:29
# @Author : cyy
# @File : 分词.py
# @desc :


import wordninja


def split_english_word(word):
    """
    # 输入英文单词
    :param word: goodsail
    :return: ['good', 'sail']
    """
    split_word = wordninja.split(word)
    return split_word


def batch_word_lst(word_lst):
    result = {}
    for word in word_lst:
        split_word = split_english_word(word)
        result[word] = split_word
    return result


if __name__ == '__main__':
    # word = input("请输入需要分词的英文单词：")
    # split_word = split_english_word(word)
    # print(split_word)

    word_lst = ['shpassion', 'goodsail', 'hikvision', 'shanghai canlang materials', 'chinatalentgroup',
                'jumbobus', 'ccbshanghai', 'becukwai', 'swirecocacolasm', 'xinyapharm', 'itwautponents',
                'goldlionchina']
    result = batch_word_lst(word_lst)
    for key, value in result.items():
        print(key, value)
