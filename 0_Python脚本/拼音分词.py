# -*- coding: utf-8 -*-
# @Time : 2022/6/2118:21
# @Author : cyy
# @File : 拼音分词.py
# @desc :


def seg(pinyin):
    """
       拼音分词,如果包括非拼音返回空
    """
    sm = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z', 'sh',
          'zh', 'ch']
    ymd = {'a': {'i': None, 'o': None, 'n': {'g': None}},
           'e': {'i': None, 'r': None, 'n': {'g': None}},
           'i': {'e': None, 'a': {'n': {'g': None}, 'o': None}, 'u': None, 'o': {'n': {'g': None}}, 'n': {'g': None}},
           'o': {'u': None, 'n': {'g': None}},
           'u': {'a': {'i': None, 'n': {'g': None}}, 'e': None, 'i': None, 'o': None}
           }
    result, i = '', 0
    while i < len(pinyin) - 1:
        if pinyin[i] in ['s', 'z', 'c'] and pinyin[i + 1] == 'h':
            result += ' ' + pinyin[i] + 'h'
            i += 2
        elif pinyin[i] in sm:
            result += ' ' + pinyin[i]
            i += 1
        else:
            result += ' '
        tmp, tmpd = '', ymd
        while i < len(pinyin):
            tmpd = tmpd.get(pinyin[i], '#')  # 如果字典中找不到则返回#
            if tmpd == '#':
                return None
            tmp += pinyin[i]
            i += 1
            if not (i < len(pinyin) and tmpd and (pinyin[i] in tmpd)):  # 循环到底,匹配到底,不明字符
                break
        result += tmp
    return result.strip()


if __name__ == '__main__':
    a = seg('xinge')
    print(a)

    # a = True
    # if not a:
    #     print("OK")


