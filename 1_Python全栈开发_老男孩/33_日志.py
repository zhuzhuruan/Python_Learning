# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------日志格式-------------------------------------------------
一、日志配置
    logging.basicConfig(
        # 1、日志输出位置：1、终端 2、文件
        # filename='access.log', # 不指定，默认打印到终端
    
        # 2、日志格式
        format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    
        # 3、时间格式
        datefmt='%Y-%m-%d %H:%M:%S %p',
    
        # 4、日志级别：默认是warning
        # critical => 50
        # error => 40
        # warning => 30
        # info => 20
        # debug => 10
        level=30,               # 修改日志级别
    )


二、输出日志
    logging.debug('调试debug')
    logging.info('消息info')
    logging.warning('警告warn')
    logging.error('错误error')
    logging.critical('严重critical')
  

-------------------------------------------------日志字典（settings.py）-------------------------------------------------
# 日志配置文件

import os

# 1、定义三种日志输出格式，日志中可能用到的格式化串如下
    # %(name)s Logger的名字
    # %(levelno)s 数字形式的日志级别
    # %(levelname)s 文本形式的日志级别
    # %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    # %(filename)s 调用日志输出函数的模块的文件名
    # %(module)s 调用日志输出函数的模块名
    # %(funcName)s 调用日志输出函数的函数名
    # %(lineno)d 调用日志输出函数的语句所在的代码行
    # %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
    # %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
    # %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
    # %(thread)d 线程ID。可能没有
    # %(threadName)s 线程名。可能没有
    # %(process)d 进程ID。可能没有
    # %(message)s用户输出的消息

# 2、强调：其中的%(name)s为getlogger时指定的名字
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

test_format = '%(asctime)s] %(message)s'

# 3、日志配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,

    # 设置可以使用的日志格式（打印或输出日志的格式，自定义配置）
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},

    # 控制日志输出的位置（日志的接收者），不同的handler会将日志输出到不同的位置
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard',
            # 可以定制日志文件路径
            # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
            # LOG_PATH = os.path.join(BASE_DIR,'a1.log')
            'filename': 'a1.log',  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        #其他的日志
        'other': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'test',
            'filename': 'a2.log',
            'encoding': 'utf-8',
        },
    },

    # 产生不同级别的日志（日志的产生者），产生的日志会传递给handler然后控制输出
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '普遍的采集': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG', # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '专门的采集': {
            'handlers': ['other',],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}


-------------------------------------------------日志产生-------------------------------------------------

# 拿到日志的产生者即loggers来产生日志

# 1-先导入日志配置字典LOGGING_DIC
import practice_file.settings as settings
from logging import config, getLogger
config.dictConfig(settings.LOGGING_DIC)

# 2-获取指定的某个logger并产生日志

# 获取logger1，产生的日志同时输出到终端和文件
logger1 = getLogger('普遍的采集')
logger1.info('这是一条info日志')

# 获取logger2，产生的日志同时只输出到终端
logger2 = getLogger('专门的采集')
logger2.info('这是一条info日志')

# 获取logger3，产生的日志同时只输出到文件
logger3 = getLogger('正常的日志')
logger3.info('这是一条info日志')


-------------------------------------------------日志名的命名-------------------------------------------------
# 日志的命名最好要以功能来命名

    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '正常采集': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG', # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '终端提示': {
            'handlers': ['console',],
            'level': 'DEBUG',
            'propagate': False,
        },
        '测试日志': {
            'handlers': ['other', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {           # 默认日志，不同情况下产生的日志都写到同一个文件下用这种默认日志
            'handlers': ['default', ],
            'level': 'DEBUG',
            'propagate': False,
        },
    },


# 拿到日志的产生者即loggers来产生日志

# 1-先导入日志配置字典LOGGING_DIC
import practice_file.settings as settings
from logging import config, getLogger
config.dictConfig(settings.LOGGING_DIC)

# 2-获取指定的某个logger并产生日志

# 获取loggers中有指定名称的logger<正常采集>
logger1 = getLogger('正常采集')
logger1.info('这是一条info日志')

# 获取loggers中有指定名称的logger<测试日志>
logger2 = getLogger('测试日志')
logger2.info('这是一条info日志')

# 获取loggers中有没有指定具体名称的logger<''>,传入的值作为日志的名称
logger3 = getLogger('用户交易')
logger3.info('这是一条info日志')
logger4 = getLogger('用户常规')
logger4.info('这是一条info日志')


-------------------------------------------------日志轮转-------------------------------------------------
# 日志记录着运行过程中的关键信息
# 日志轮转：当日志文件达到指定的大小，会将日志文件进行切分，把老日志logger1.log重命名，新建日志logger1，将新纪录的日志写到logger1中
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard',
            'filename': DEFAULT_LOG_PATH,   # 日志文件
            'maxBytes': 1024*1024*5,   # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },



# 1-先导入日志配置字典LOGGING_DIC
import practice_file.settings as settings
from logging import config, getLogger
config.dictConfig(settings.LOGGING_DIC)

# 2-获取指定的某个logger并产生日志
logger3 = getLogger('用户交易')
logger3.info('这是一条info日志')

         
"""
