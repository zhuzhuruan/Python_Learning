# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------hash-------------------------------------------------
一、什么是哈希hash
1、定义：hash是一种算法（python3.x里代替了md5模块和sha模块，主要提供SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5算法），
       该算法接受传入的内容，经过运算得到一串hash值
       
2、特点：
    （1）只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
    （2）不能由hash值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码
    （3）只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的
   
   
二、哈希hash的用途
    1、特点（2）用于密码、密文的传输与验证
    2、特定（1）（3）用于文件的完整性校验  
   

三、如何使用hashlib
    hash算法就像一座工厂，工厂接收你送来的原材料（可以用m.update()为工厂运送原材料），经过加工返回的产品就是hash值
    
    （1）用途（2）（3）的使用
    
            import hashlib
            m1 = hashlib.md5()
            m1.update('hello'.encode('utf-8'))
            m1.update('world'.encode('utf-8'))
            res1 = m1.hexdigest()
            print(res1)
                    
            m2 = hashlib.md5('hell'.encode('utf-8'))
            m2.update('o'.encode('utf-8'))
            m2.update('wor'.encode('utf-8'))
            m2.update('ld'.encode('utf-8'))
            res2 = m2.hexdigest()
            print(res2)
        
    （1）用途（1）密码加盐的使用
            
            # 模拟撞库
            
                import hashlib
                
                correct_pwd = '136399a18f481ad14bbba3cd1c768645'
                guess_pwd = ['cyy19980101', '19980101cyy', 'Cyy19980101', 'CYY1998', '1998CYY0101']
                pwd_dic = {}
                for pwd in guess_pwd:
                    hash_pwd = hashlib.md5(pwd.encode('utf-8'))
                    pwd_dic[pwd] = hash_pwd.hexdigest()
                
                for key, value in pwd_dic.items():
                    if value == correct_pwd:
                        print('撞库成功，明文密码是：%s' % value)
                        break
                else:
                    print('撞库失败')
    
    
            # 提升撞库成本=====>密码加盐(在密码的前后中添加一些干扰字符)
            
                import hashlib
                
                # 密码加盐
                correct_pwd = hashlib.md5()
                correct_pwd.update('天王'.encode('utf-8'))
                correct_pwd.update('Cyy19980101'.encode('utf-8'))
                correct_pwd.update('盖地虎'.encode('utf-8'))
                correct_pwd_salt = correct_pwd.hexdigest()
                
                guess_pwd = ['cyy19980101', '19980101cyy', 'Cyy19980101', 'CYY1998', '1998CYY0101']
                pwd_dic = {}
                for pwd in guess_pwd:
                    hash_pwd = hashlib.md5(pwd.encode('utf-8'))
                    pwd_dic[pwd] = hash_pwd.hexdigest()
                
                for key, value in pwd_dic.items():
                    if value == correct_pwd_salt:
                        print('撞库成功，明文密码是：%s' % value)
                        break
                else:
                    print('撞库失败')
            
            
"""

