# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------序列化-------------------------------------------------
一、什么是序列化
    指的是把内存中的数据类型转换成一种特定格式的内容，该格式的内容可用于存储或传输给其他平台使用
        
        内存中的数据类型----->序列化----->特定的格式(json/pickle)
        特定的格式----->序列化----->内存中的数据类型

二、为何要序列化
    1、序列化得到的结果----->特定的格式的内容有两种用途
        （1）可用于存储------>用于存档
        （2）传输给其他平台使用------>跨平台数据交互
        
    2、针对用途（1）的特定格式:应该是一种Python专用的格式=====》pickle
       针对用途（2）的特定格式：应该是一种通用的、能够被所有语言识别的一种格式=====》json

三、如何序列化和反序列化
（一）json
    1、序列化：
        （1）针对内存对象：json.dumps()       
                    lst = [1, 'aaa', 2, 'bbb', 3, 'ccc']
                    lst_json = json.dumps(lst)
                    with open(file, 'wt', encoding='utf-8') as f:
                        f.write(lst_json)
                        
        （2）针对文件句柄：json.dump()
                    lst = [1, 'aaa', 2, 'bbb', 3, 'ccc']
                    with open(file, 'wt', encoding='utf-8') as f:
                        json.dump(lst, f)
        
        
    2、反序列化：
        （1）针对内存对象：json.loads()
                    with open(file, 'rt', encoding='utf-8') as f:                        
                        lst_json = f.read()
                        lst = json.loads(lst_json)
                                           
        （2）针对文件句柄：json.load()
                    with open(file, 'rt', encoding='utf-8') as f:                        
                        lst = json.load(f)
                        
    3、注意
        （1）json格式兼容的是所有语言通用的数据类型，不包括某种语言特有的数据类型
                json.dumps({1,2,3,4,5})
                
        （2）注意区分python格式和json格式    
                # json格式
                    json.loads([1, "aaa", true, false]) 
                # python格式
                    [1, 'aaa', "aaa", TRUE, True, False, FALSE]        
                    
                    
（二）pickle
    1、序列化：
        （1）针对内存对象：pickle.dumps()       
                    lst = [1, 'aaa', 2, 'bbb', 3, 'ccc']
                    lst_pickle = pickle.dumps(lst)
                    with open(file, 'wb') as f:
                        f.write(lst_pickle)
                        
        （2）针对文件句柄：pickle.dump()
                    lst = [1, 'aaa', 2, 'bbb', 3, 'ccc']
                    with open(file, 'wb') as f:
                        pickle.dump(lst, f)
        
    2、反序列化：
        （1）针对内存对象：pickle.loads()
                    with open(file, 'rb') as f:
                        lst_pickle = f.read()
                        lst = pickle.loads(lst_pickle)
                                           
        （2）针对文件句柄：pickle.load()
                    with open(file, 'rb') as f:                        
                        lst = pickle.load(f)
                        
                                                
"""

