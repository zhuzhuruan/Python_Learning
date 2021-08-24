# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------sys模块-------------------------------------------------
一、基本功能
    sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
    sys.argv           命令行参数List，第一个元素是程序本身路径(在Python程序内，接收一个来自外界的参数)

            # 源代码
            import sys
            src_file = sys.argv[1]
            dst_file = sys.argv[2]
            
            with open(r'%s' % src_file, 'rt', encoding='utf-8') as read_f, open(r'%s' % dst_file, 'wt', encoding='utf-8') as write_f:
                for line in read_f:
                    write_f.write(line)
            
            # 窗口执行
            #     >>> python 28_模块.py src_file dst_file
            


-------------------------------------------------打印进度条-------------------------------------------------
import time

def progress(percent):
    res = int(50 * percent) * '▉'
    print('\r%-50s %d%%' % (res, int(100 * percent)), end='')


def main(download_size, total_size, gap_size):
    while download_size < total_size:
        time.sleep(0.01)
        if total_size - download_size > gap_size:
            download_size += gap_size
        else:
            download_size += (total_size - download_size)
        percent = download_size/total_size
        progress(percent)


if __name__ == '__main__':
    main(0, 1025011, 1024)


"""