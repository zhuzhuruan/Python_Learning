# -*- coding:utf-8 -*-
import jieba

"""
---------------------------------------------------------知识点---------------------------------------------------------
"""

"""
-----------------------------集合----------------------------
集合是多个元素的无序组合:
    -- 集合类型与数学中的集合概念一致
    -- 集合元素之间无序，每个元素唯一，不存在相同元素
    -- 集合用{}表示，元素间用逗号分割
    -- 建立集合类型用{} 或set()

集合操作符：
    -- S|T : 并，返回一个新集合，包括在集合S和集合T中的所有元素
    -- S-T : 差，返回一个新集合，包括在集合S但不在T中的元素
    -- S&T : 交，返回一个新集合，包括同时在集合S和集合T中的元素
    -- S^T : 补，返回一个新集合，包括集合S和T中的非相同元素
    -- S <= T 或 S < T : 返回True(False)，判断S和T的子集关系    
    
集合增强操作符：
    -- S|T : 并，更新集合S，包括在集合S和集合T中的所有元素
    -- S-T : 差，更新集合S，包括在集合S但不在T中的元素
    -- S&T : 交，更新集合S，包括同时在集合S和集合T中的元素
    -- S^T : 补，更新集合S，包括集合S和T中的非相同元素
    
集合的处理方法:
    -- S.add(x): 如果x不在集合S中，将x增加到集合
    -- S.discard(x): 移除S中元素x，如果x不在集合S中，不报错
    -- S.remove(x): 移除S中元素x，如果x不在集合S中，产生KeyError异常
    -- S.clear(): 移除S中的所有元素
    -- S.pop(): 随即返回S中的一个元素，更新S，若S为空产生KeyError异常
    -- S.copy(): 返回集合S的一个副本
    -- len(S): 返回集合S的一个副本
    -- set(x): 讲其他类型变量x转变为集合类型
    

---------------------------------序列-----------------------------
序列是具有先后关系的一组元素
    -- 序列是一维元素向量，元素类型可以不同
    -- 序列是一个基类类型：字符串、元组、列表

序列通用函数和方法：
    -- len(s): 返回序列s的长度，即元素个数
    -- min(s)、max(x): 返回序列s的最小、大元素，s中元素需要可比较
    -- s.index(x)或s.index(x,i,j): 返回序列s从i开始到j位置中第一次出现元素x的位置
    -- s.count(x): 返回序列s中出现x的次数
    
    
---------------------------------元组-----------------------------
元组是序列类型的一种扩展：
    -- 元组是一种序列类型，一旦创建就不能被修改
    -- 使用()或tuple()创建，元素间用逗号分隔
    -- 可以使用()或不使用()创建


---------------------------------列表-----------------------------
列表是序列类型的一种扩展：
    -- 列表是序列类型的一种扩展，创建后可以随意被修改
    -- 使用[]或list()创建，元素间用逗号分隔
    
列表操作函数和方法：
    -- ls.append(): 在列表ls的最后增加一个元素x
    -- ls.clear(): 删除列表ls中的所有元素
    -- ls.copy(): 生成一个新列表，赋值ls中的所有元素
    -- ls.insert(i, x): 在列表ls中的第i位置增加元素x
    -- ls.pop(i): 将列表ls中的第i位置元素取出并删除该元素
    -- ls.remove(x): 将列表ls中出现的第一个元素x删除
    -- ls.reverse(): 将列表ls中的元素反转


---------------------------------字典-----------------------------
字典类型是“映射”的体现：
    -- 键值对： 键是数据索引的扩展
    -- 字典是键值对的集合，键值对之间无序
    -- 采用{}或dict()创建，键值对用:表示
    

---------------------------------jieba分词-----------------------------
分词原理：jieba分词依靠中文词库
    -- 利用一个中文词库，确定汉字之间的关联概率
    -- 汉字间概率大的组成词组，形成分词结果
    -- 除了分词，用户还可以添加自定义的词组

三种模式：
    -- 精确模式：把文本精确的切分开，不存在冗余单词
    -- 全模式：把文本中所有可能的词语都扫描出来，有冗余
    -- 搜索引擎模式：在精确模式的基础上，对长词再次切分
    
常用函数：
    -- jieba.lcut(s): 精确模式，返回一个列表类型的分词结果
    -- jieba.lcut(s, cut_all=True): 全模式，返回一个列表类型的分词结果，存在冗余
    -- jieba.lcut_for_search(s): 搜索引擎模式，返回一个列表类型的分词结果，存在冗余
    -- jieba.add_word(w): 向分词词典增加新词w
         
"""
"""
---------------------------------------------------------实例---------------------------------------------------------
"""


def getNum():
    nums = []
    iNumStr = input("请输入数字(回车退出):")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出):")
    return nums


# 计算平均值
def mean(numbers):
    s = 0
    for num in numbers:
        s = s + num
    return s / len(numbers)


# 计算方差
def dev(numbers, mean):
    sdev = 0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


# 计算中位数
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med


def main():
    n = getNum()
    m = mean(n)
    print("平均值:{},方差:{},中位数:{}.".format(m, dev(n, m), median(n)))


# 文本词频统计
# 英文文献
def getText():
    txt = open("分词文件//hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_“{|}~':
        txt.replace(ch, " ")
    return txt


def Text_Main():
    hamletTxt = getText()
    words = hamletTxt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1  # get() 函数返回指定键的值:dict.get(key, default=None)
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较。
    for i in range(10):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


# 中文文献
def get_word_cut():
    txt = open("分词文件//threekingdoms.txt", "r", encoding="utf-8").read()
    excludes = {'将军', '却说', '荆州', '二人', '不可', '不能', '如此', '商议', '如何', '军士', '左右', '军马', '引兵', '次日',
                '大喜', '天下', '东吴', '于是', '今日', '不敢', '魏兵', '一人', '都督', '人马', '不知', '陛下', '后主', '众将',
                '汉中', '只见', '蜀兵', '上马', '大叫', '太守', '此人', '夫人', '先主', '后人', '背后', '城中', '天子'}
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        elif word == '诸葛亮' or word == '孔明曰':
            rword = "孔明"
        elif word == '关公' or word == '云长':
            rword = "关羽"
        elif word == '玄德' or word == '玄德曰' or word == '主公':
            rword = "刘备"
        elif word == '孟德' or word == '丞相':
            rword = "曹操"
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1
    for word in excludes:
        del counts[word]
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    """
        把lambda函数作为变量赋值给Key,作用于items中的每一个元素
    """

    for i in range(15):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


if __name__ == "__main__":
    # a = set("pypy123")
    # print(a)
    # main()
    # Text_Main()
    get_word_cut()
