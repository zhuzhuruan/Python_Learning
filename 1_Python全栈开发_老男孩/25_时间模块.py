# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------时间模块-------------------------------------------------
一、time
1、时间格式
    （1）时间戳：用于时间间隔的计算
            time.time()
                
    （2）格式化时间：按照某种格式显示的时间：用于时间的展示
            time.strftime('%Y-%m-%d %H:%M:%S %p')
                
    （3）结构化时间：用于单独获取时间的一部分
            time.localtime()        # 当前地区的时区
            time.gmtime()           # UTC时区（0时区）
            time.localtime().tm_year        # 获取结构化时间中的某个部分 
     
     
 二、datetime
    （1）格式化时间
            datetime.datetime.now()
    
    （2）时间的计算
            datetime.datetime.now() + datetime.timedelta(days=3)        # 当前时间往后推3天
            datetime.datetime.now() + datetime.timedelta(weeks=-3)        # 当前时间往前推3周
       
       
三、格式转换
1、结构化时间 -> 时间戳
    time.mktime(time.localtime())
    
2、时间戳 -> 结构化时间
    time.localtime(time.time())

3、结构化时间 -> 格式化时间
    time.strftime('%Y-%m-%d %H:%M:%S %p', time.localtime())

4、格式化时间 -> 结构化时间
    time.strptime('2021-8-23 16:30:23', '%Y-%m-%d %H:%M:%S')
       
5、格式化时间 -> 时间戳          # 不能直接转，格式化时间 -> 结构化时间 -> 时间戳
    struct_time = time.strptime('2021-8-23 16:30:23', '%Y-%m-%d %H:%M:%S')
    timestamp = time.mktime(struct_time) + 7*24*60*60
    print(timestamp)
    
   时间戳 -> 格式化时间 
    struct_time = time.localtime(timestamp)
    format_time = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
    print(format_time)


四、其他知识
time.sleep()        # 休眠时间
time.asctime()      # Linux系统
datetime.datetime.utcnow()      # 世界标准时间
datetime.datetime.fromtimestamp(timestamp)      # 时间戳 -> 格式化时间       
    
                 
"""
import time
print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
print(time.strftime('%Y-%m-%d %H:%M:%S %p', time.localtime()))
print(time.localtime())
print(time.gmtime())


import datetime
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days=3))
print(datetime.datetime.now() + datetime.timedelta(weeks=4))


struct_time = time.strptime('2021-8-23 16:30:23', '%Y-%m-%d %H:%M:%S')
timestamp = time.mktime(struct_time) + 7*24*60*60
print(timestamp)

struct_time = time.localtime(timestamp)
format_time = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
print(format_time)

print(datetime.datetime.fromtimestamp(timestamp))