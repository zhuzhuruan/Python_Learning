# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------random模块-------------------------------------------------
一、基本用法

    import random
    print(random.random())      # [0, 1)之间的小数
    print(random.randint(1, 10))        # [1, 10]之间的整数
    print(random.randrange(1, 10))      # [1, 10)之间的整数
    print(random.choice([1, 'a', {'name':'cyy', 'age':23}]))    # 随机取出列表中的其中一个元素，不限类型
    print(random.sample([1, 'a', {'name':'cyy', 'age':23}], 2))     # # 随机取出列表中的多个元素，不限类型
    print(random.uniform(1, 10))      # (1, 10)之间的小数
    
    lst = [1, 3, 5, 7, 9]
    random.shuffle(lst)      # 随机打乱列表的顺序
    print(lst)

     
二、应用：随机验证码   

    import random
    def get_random_code(code_length):
        identifying_code = ''
        for i in range(code_length):
            letter = chr(random.randint(65, 90))        # 随机大写字母
            number = str(random.randint(0, 9))          # 随机整数
            identifying_code += random.choice([letter, number])
        return identifying_code
    
    identifying_code = get_random_code(6)
    print(identifying_code)
    
    
  
     
                 
"""

import random


def get_random_code(code_length):
    identifying_code = ''
    for i in range(code_length):
        letter = chr(random.randint(65, 90))  # 随机大写字母
        number = str(random.randint(0, 9))  # 随机整数
        identifying_code += random.choice([letter, number])
    return identifying_code


identifying_code = get_random_code(6)
print(identifying_code)
