# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------configparser模块-------------------------------------------------
1、定义：configparser模块是用来加载某种特殊的配置文件的

        # 注释1
        ; 注释2
        
        [section1]
        k1 = v1
        k2:v2
        user=egon
        age=18
        is_admin=true
        salary=31
        
        [section2]
        k1 = v1
             
             
2、功能

    import configparser
    
    config = configparser.ConfigParser()
    config.read('practice_file/configparser配置文件.cfg')
    
    # 查看所有的标题
    res = config.sections()
    print(res)
    
    # 查看标题section1下所有key=value的key
    options = config.options('section1')
    print(options)
    
    #查看标题section1下所有key=value的(key,value)格式
    item_list = config.items('section1')
    print(item_list)
    
    #查看标题section1下user的值=>字符串格式
    val = config.get('section1', 'user')
    print(val)
    
    #查看标题section1下age的值=>整数格式
    val1=config.getint('section1','age')
    print(val1)
    
    #查看标题section1下is_admin的值=>布尔值格式
    val2=config.getboolean('section1','is_admin')
    print(val2)
    
    #查看标题section1下salary的值=>浮点型格式
    val3=config.getfloat('section1','salary')
    print(val3)
                     
"""
