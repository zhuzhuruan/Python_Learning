# -*- coding:utf-8 -*-
import turtle as t
from PIL import Image
import numpy
import wordcloud
import jieba
from imageio import imread

"""
---------------------------------------------------------知识点---------------------------------------------------------
"""

"""
-----------------------------文件的使用----------------------------
文件的类型：
    -- 文件是数据的抽象和集合
        -- 文件是存储在辅助存储器上的数据序列
        -- 文件是数据存储的一种形式
        -- 文件展现形态：文本文件和二进制文件
    -- 文本文件
        -- 由单一特定编码组成的文件，如utf-8编码
        -- 由于存在编码，也被看成是存储着的长字符
        -- 适用于例如：.txt文件、.py文件
    -- 二进制文件
        -- 直接由比特0和1组成，没有统一字符编码
        -- 一般存在二进制0和1的组织结构，即文件格式
        -- 适用于例如：.png文件、.avi文件
        
文件的打开和关闭：
    -- 文件的打开
        -- <变量名> = open(<文件名>, <打开模式>)
            -- <变量名>：文件句柄
            -- <文件名>：文件路径和名称
            -- <文本 or 二进制>：读 or 写
        -- 打开模式
            -- 'r': 只读模式，默认值，如果文件不存在，返回FileNotFoundError
            -- 'w': 覆盖写模式，文件不存在则创建，存在则完全覆盖
            -- 'x': 创建写模式，文件不存在则创建，存在则返回FileExistsError
            -- 'a': 追加写模式，文件不存在则创建，存在则在文件最后追加内容
            -- 'b': 二进制文件模式
            -- 't': 文本文件模式，默认值  
            -- '+': 与r/w/x/a一同使用，在原功能基础上增加同时读写功能
    -- 文件的关闭
        -- <变量名>.close()
               
文件内容的获取:
    -- <f>.read(size=-1): 读入全部内容，如果给出参数，读入前size长度
    -- <f>.readline(size=-1): 读入一行内容，如果给出参数，读入改行前size长度
    -- <f>.readlines(hint=-1): 读入文件所有行，以每行为元素形成列表，如果给出参数，读入前hint行
    
数据文件的写入：
    -- <f>.write(s): 向文件写入一个字符串或字节流
    -- <f>.writelines(lines): 将一个元素全为字符串的列表写入文件（直接拼接不换行）
    -- <f>.seek(offset): 改变当前文件操作指针的位置，offset含义如下：0-文件开头；1-当前位置；2-文件结尾
    
    
-----------------------------自动轨迹绘制----------------------------
基本思路
    -- 定义数据文件格式（接口）
    -- 编写程序，根据文件接口解析参数绘制图形
    -- 编制数据文件
    
数据接口定义
    -- 300, 0, 144, 1, 0, 0
        -- 300：行进距离
        -- 0或1：0-左转；1-右转
        -- 144：转向角度
        -- 1,0,0：RGB三个通道的颜色
        
        
-----------------------------数据的维度----------------------------
一维数据
    -- 由对等关系的有序或无序数据构成，采用线性方式组织
    -- 对应列表、数组、集合等概念
    
二维数据
    -- 由多个一维数据构成，是一维数据的组合形式
    -- 表格是典型的二维数据
    
多维数据
    -- 由一维或二维数据在新维度上扩展生成
    
高维数据
    -- 仅利用最基本的二元关系展示数据间的复杂结构
    -- 例如键值对
    
一维数据的格式化和处理
    -- 数据的维度：一维、二维、多维、高维
    -- 一维数据的表示：列表类型（有序）和集合类型（无序）
    -- 一维数据存储：空格分隔、逗号分隔，特殊符号分隔
    -- 一维数据的处理：字符串方法.split() 和 .join()
    
二维数据的格式化和处理
    -- 二维数据的表示：列表类型，其中每个元素也是一个列表、
    -- CSV格式：逗号分隔表示一维，按行分隔表示二维
    -- 二维数据的处理：for循环+.split()和.join()


-----------------------------wordcloud库----------------------------
wordcloud库把词云当做一个WordCloud对象
    -- wordcloud。WordCloud()代表一个文本对应的词云
    -- 可以根据文本中词语出现的频率等参数绘制词云
    -- 词云的绘制形状、尺寸和颜色都可以设定

wordcloud库常规方法：
    -- w = wordcloud.WordCloud(<参数>)
        -- width: 指定词云对象生成图片的宽度，默认400像素
        -- height: 指定词云对象生成图片的高度，默认200像素
        -- min_font_size: 指定词云中字体的最小字号，默认4号
        -- max_font_size: 指定词云中字体的最大字号，根据高度自动调节
        -- font_step: 指定词云中字体字号的步长间隔，默认为1
        -- font_path: 指定字体文件的路径，默认None
        -- max_words: 指定词云显示的最大单词数量，默认200
        -- stop_words: 指定词云的排除词列表，即不显示的单词列表
        -- mask: 指定词云形状，默认为长方形，需要引用imread()函数
            -- from scipy.misc import imread
               mk = imread("pic.png")
               w = wordcloud.WordCloud(mask=mk)
        -- background_color: 指定词云图片的背景颜色，默认为黑色               
    -- w.generate(): 向WordCloud对象w中加载文本txt
    -- w.to_file(filename): 将词云输出为图像文件, .png或.jpg格式
  

"""
"""
---------------------------------------------------------实例---------------------------------------------------------
"""


# 数据的写入

def WriteTest_V1():
    fo = open('分词文件\\output.txt', 'w+')
    ls = ['苹果', '香蕉', '梨子']
    fo.writelines(ls)
    for line in fo:
        print(line)  # 没有任何输出，因此此时文件操作的指针在文件的最后一行，往后读取不到数据
    fo.close()


def WriteTest_V2():
    fo = open('分词文件\\output.txt', 'w+')
    ls = ['苹果', '香蕉', '梨子']
    fo.writelines(ls)
    fo.seek(0)
    for line in fo:
        print(line)
    fo.close()


# 自动轨迹绘制
def AutoTraceDraw():
    t.title('自动轨迹绘制')
    t.setup(800, 600, 0, 0)
    t.pencolor("red")
    t.pensize(5)
    # 数据获取
    datals = []
    f = open("分词文件\\output.txt")
    for line in f:
        line = line.replace("\n", "")
        datals.append(list(map(eval, line.split(","))))
        """
            map()函数
                -- 是Python提供的内嵌函数，无需import
                -- 作用: 将第一个参数的功能作用于第二个参数的每个元素
                        第一个参数是函数的名字，第二个参数是迭代类型            
        """

    f.close()
    # 自动绘制
    for i in range(len(datals)):
        t.pencolor(datals[i][3], datals[i][4], datals[i][5])
        t.fd(datals[i][0])
        if datals[i][1]:
            t.right(datals[i][2])
        else:
            t.left(datals[i][2])


# 基础词云绘制
def wordcloud_v1():
    """
    1、分隔：以空格分隔单词
    2、统计：单词出现次数并过滤
    3、字体：根据统计配置字号
    4、布局：颜色环境尺寸
    """
    txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，它按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理"
    w = wordcloud.WordCloud(width=1000, height=700, font_path="msyh.ttc")
    w.generate(" ".join(jieba.lcut(txt)))  # 中文需要先分词并组成空格分隔字符串
    w.to_file("分词文件\\pywcloud.png")


# 词云-政府工作报告
def GovRptWordCloudv1():
    # mask = numpy.array(Image.open("分词文件\\fivestart.png"))
    mask = imread("分词文件\\fivestart.png")
    f = open("分词文件\\新时代中国特色社会主义.txt", "r", encoding="utf-8")
    t = f.read()
    f.close()
    ls = jieba.lcut(t)
    txt = " ".join(ls)
    w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, background_color="white",
                            max_words=200, mask=mask)
    w.generate(txt)
    w.to_file("分词文件\\grwordcloud_fivestart.png")


if __name__ == "__main__":
    # WriteTest_V2()
    # AutoTraceDraw()
    # wordcloud_v1()
    GovRptWordCloudv1()