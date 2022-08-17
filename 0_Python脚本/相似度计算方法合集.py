# -*- coding: utf-8 -*-
# @Time : 2022/6/1416:17
# @Author : cyy
# @File : 相似度计算方法合集.py
# @desc :

import Levenshtein
from nltk.corpus import wordnet as wn

VALUE = 0.9
METHOD = 'leven'


def similarity(word1, word2, method):
    if method == 'edit':
        return editSim(word1, word2)
    elif method == 'hamming':
        return hammingSim(word1, word2)
    elif method == 'leven':
        return levenSim(word1, word2)
    elif method == 'jaro':
        return jaroSim(word1, word2)
    elif method == 'jaro_winkler':
        return jaroWinklerSim(word1, word2)
    elif method == 'lcs':
        return lcsSim(word1, word2)
    elif method == 'dice':
        return diceSim(word1, word2)
    elif method == 'wordnet':
        return wordnetSim(word1, word2)


def editSim(word1, word2):
    """
    按照编辑距离，计算两个词的编辑相似度。单纯使用编辑距离/较长词
    :param word1: 词
    :param word2: 词
    :return: 编辑相似度
    """
    n = max(len(word1), len(word2))
    return 1 - Levenshtein.distance(word1, word2) / n


def hammingSim(word1, word2):
    """
    按照汉明距离，计算两个词的汉明相似度。单纯使用汉明距离 / 较长词。由于汉明距离计算要求两个word的长度必须一致，因此对长的词采用单纯的截断的方式
    从前面截断、从后面截断
    :param word1: 词
    :param word2: 词
    :return: 汉明相似度
    """
    # 从前面截断
    n = max(len(word1), len(word2))
    if len(word1) > len(word2):
        word3 = word1[:len(word2)]
        return (len(word2) - Levenshtein.hamming(word3, word2)) / n
    else:
        word3 = word2[:len(word1)]
        return (len(word1) - Levenshtein.hamming(word1, word3)) / n
    """
    #从后面截断
    n =max(len(word1), len(word2))
    if len(word1) > len(word2):
        word3 =word1[len(word1)-len(word2):]
        return (len(word2) - Levenshtein.hamming(word3, word2)) / n
    else:
        word3 =word2[len(word2)-len(word1):]
        return (len(word1) - Levenshtein.hamming(word1, word3)) / n
    """


def levenSim(word1, word2):
    """
    计算莱文斯坦比。计算公式 (sum–ldist)/sum,其中sum是指word1和word2字串的长度总和，ldist是类编辑距离。
    注意这里是类编辑距离，不是通常所说的编辑距离，在类编辑距离中删除、插入依然+1，但是替换+2
    :param word1: 词
    :param word2: 词
    :return: 莱文斯坦比
    """
    return Levenshtein.ratio(word1, word2)


def jaroSim(word1, word2):
    """
    计算jaro距离。
    :param word1: 词
    :param word2: 词
    :return: jaro距离
    """
    return Levenshtein.jaro(word1, word2)


def jaroWinklerSim(word1, word2):
    """
    计算Jaro–Winkler距离，而Jaro-Winkler则给予了起始部分就相同的字符串更高的分数
    :param word1: 词
    :param word2: 词
    :return: Jaro–Winkler距离
    """
    return Levenshtein.jaro_winkler(word1, word2)


def lcsSim(word1, word2):
    """
    value越小，速度越快&#xff08;value&#61;0.5时，时间&#61;5~10min，慢&#xff09;
    LCS，计算两个词的最长公共子序列长度。单纯使用lcs/较长词。
    :param word1: 词
    :param word2: 词
    :return: LCS/n
    """
    n = max(len(word1), len(word2))
    dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
    for i in range(len(word1) - 1, -1, -1):  # 倒序，简化边界条件判断
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0] / n


def diceSim(word1, word2):
    """
    计算Dice距离，其用于度量两个集合的相似性，因为可以把字符串理解为一种集合，因此Dice距离也会用于度量字符串的相似性。
    此外，Dice系数的一个非常著名的使用即实验性能评测的F1值
    :param word1: 词
    :param word2: 词
    :return: Dice距离
    """
    a_bigrams = set(word1)
    b_bigrams = set(word2)
    overlap = len(a_bigrams & b_bigrams)
    return overlap * 2.0 / (len(a_bigrams) + len(b_bigrams))


def wordnetSim(word1, word2):  ##有问题?
    """
    语义相似度，基于wordnet
    计算词语相似度时，总以包含词语概念的语义相似度的最大值来表示词语的语义相似度，将其也应用于短文本;短语;，即基于最大值的短文本语义相似度
    ##对于短语中部分词相等的处理
    :param word1: 词
    :param word2: 词
    :return: 基于最大值的wordnet的语义相似度
    """
    phrase1 = word1
    phrase2 = word2
    word1 = phrase1.split(' ')
    word2 = phrase2.split(' ')
    path_sim = 0
    for w1 in word1:
        for w2 in word2:
            synsets1 = wn.synsets(w1)
            synsets2 = wn.synsets(w2)
            # path_sim =0
            for tmpword1 in synsets1:
                for tmpword2 in synsets2:
                    if tmpword1.pos() == tmpword2.pos():
                        try:  # 对于短语中部分词相等的处理
                            sim = tmpword1.path_similarity(tmpword2)
                            if w1 != w2:  # 对于短语来说，不能将其中一个词相等，则短语完全相等
                                path_sim = max(path_sim, sim)  # 取最大值
                        except Exception as e:
                            continue
                            # print(tmpword1, tmpword2)
                            # print("path: " + str(e))
    return path_sim


"""
词形还原
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
aa =lemmatizer.lemmatize(&#39;recognitions&#39;)
print(aa)
"""

if __name__ == '__main__':
    method_lst = ['edit', 'hamming', 'leven', 'jaro', 'jaro_winkler', 'lcs', 'dice', 'wordnet']
    # 测试
    word1 = 'lan'
    word2 = 'goldlion air'
    for method in method_lst:
        print(method, similarity(word1, word2, method))
    #
    # 批量
    # word_compare_dic = {'shpassion': 'ChinaNet-sHPa-5G',
    #                     'goodsail': 'sailling',
    #                     'hikvision': 'hik-office',
    #                     'shanghai canlang materials': 'lan chang',
    #                     'chinatalentgroup': 'TalentCanteen',
    #                     'jumbobus': 'JumboGroup',
    #                     'ccbshanghai': 'CCB-jizhong',
    #                     'becukwai': 'kwai-restroom',
    #                     'swirecocacolasm': 'swire_guest',
    #                     'xinyapharm': 'xinyait',
    #                     'itwautponents': 'ITWAutoChina_Production',
    #                     'goldlionchina': 'GoldLion Air'}
    # for word1, word2 in word_compare_dic.items():
    #     print("===============", word1, word2, "===============")
    #     for method in method_lst:
    #         print(method, similarity(word1, word2, method))
    #
    # print(similarity('sailing', 'sailing', 'wordnet'))
