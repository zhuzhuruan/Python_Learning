# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------算法--二分法-------------------------------------------------
# 需求：按照从小到大顺序排列的列表，需要从该数字列表中找到想要的那一个数字,如何做更高效？
        # 一般方式：效率太低
                lst = [1, 4, 6, 9, 10, 23, 26, 32, 38, 45, 48, 56]
                target = 38
                for i_index, i in enumerate(lst):
                    if i == target:
                        print(i_index, "find it")
                        break
                
        # 二分法
                     
                lst = [1, 4, 6, 9, 10, 23, 26, 32, 38, 45, 48, 56, 78]
                target = 38
                
                def binary_search(lst, target):
                    # print(lst)
                    if len(lst) == 1:
                        print("查找的目标值不存在")
                        return
                    # 找到列表的中间值
                    mid_value = lst[len(lst)//2]
                    if target > mid_value:
                        # 查找列表的右半部分
                        new_lst = lst[len(lst)//2+1:]
                        binary_search(new_lst, target)
                    elif target < mid_value:
                        # 查找列表的左半部分
                        new_lst = lst[:len(lst) // 2]
                        binary_search(new_lst, target)
                    else:
                        print("find it")
                
                binary_search(lst, target)              
                

-------------------------------------------------面向过程的变成思想-------------------------------------------------
       
面向过程的编程思想：
    # 定义
        （1）核心是“过程”两个字，过程即流程，指的是做事的步骤：先做什么、再做什么、最后做什么
        （2）基于该思想编写程序就好比设计一条流水线
    
    # 优缺点
        （1）优点：复杂的问题流程化、简单化
        （2）缺点：扩展性非常差   
        
    # 应用场景解析
        （1）不是所有的软件都需要频繁更迭：比如编写脚本
        （2）即使是一个软件需要频繁更迭，也不代表这个软件的所有组成部分都需要一起更迭
       
       
                 
"""
