# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------subprocess模块-------------------------------------------------
1、subprocess模块是用来执行系统命令的

        import subprocess
        
        obj = subprocess.Popen('D:/', shell=True,       # 输入要执行的命令，相当于打开cmd
                               stdout=subprocess.PIPE,      # 将命令执行成功的结果扔到管道中
                               stderr=subprocess.PIPE       # 将命令执行失败的结果扔到管道中
                               )
        
        # 查看正确管道中的信息，根据系统编码进行解码
        res_out = obj.stdout.read().decode('gbk')       
        print(res_out)
        
        # 查看错误管道中的信息，根据系统编码进行解码
        res_err = obj.stderr.read().decode('gbk')
        print(res_err)
  


               
"""