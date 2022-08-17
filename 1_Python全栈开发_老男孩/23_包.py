# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------包-------------------------------------------------
一、什么是包
1、定义：包就是包含有__init__.py文件的文件夹

2、包的本质是模块的一种形式，用来被当做模块导入
    
    import package_m发生的三件事：            
        （1）产生一个名称空间
        （2）运行包下的__init__.py文件，将运行过程中产生的名字放到（1）的名称空间中
        （3）在当前执行文件的名称空间中拿到包的名字，该名字指向（1）的名称空间

    注意：
        1. 在python3中，即使包下没有__init__.py文件，import 包仍然不会报错，而在python2中，包下一定要有该文件，否则import包报错
        2. 创建包的目的不是为了运行，而是被导入使用，记住，包只是模块的一种形式而已，包的本质就是一种模


二、为什么要有包
    随着模块数目的增多，把所有模块不加区分地放到一起也是极不合理的，于是Python为我们提供了一种把模块组织到一起的方法，即创建一个包。
包就是一个含有__init__.py文件的文件夹，文件夹内可以组织子模块或子包。例如原本把所有功能都写在package_m.py模块中，随着功能的增加，
管理难度增加，因此把package_m.py模块中的功能分散在mm1.py、mm2.py和mm3.py三个文件中，把这三个文件放在名为package_md的包下。


三、如何导入包
1、绝对导入: 以顶级包为起始

    # 执行文件
        import practice_file.package_m as f      # import __init__.py
        f.func1()
        f.func2()
        f.func3()
        f.func4()
    
    # __init.py__文件
        from practice_file.package_m.mm1 import func1
        from practice_file.package_m.mm2 import func2
        from practice_file.package_m.mm3 import func3
        from practice_file.package_m.son_m.mm3 import func4,func5
    
注意：
    1.关于包相关的导入语句也分为import和from ... import ...两种，但是无论哪种，无论在什么位置，在导入时都必须遵循一个原则：凡是在导入时带点的，
      点的左边都必须是一个包，否则非法。可以带有一连串的点，如import 顶级包.子包.子模块,但都必须遵循这个原则。但对于导入后，在使用时就没有这种限制了，
      点的左边可以是包,模块，函数，类(它们都可以用点的方式调用自己的属性)。
    
    2、包A和包B下有同名模块也不会冲突，如A.a与B.a来自俩个命名空间
    
    3、import导入文件时，产生名称空间中的名字来源于文件，import 包，产生的名称空间的名字同样来源于文件，即包下的__init__.py，导入包本质就是在导入该文件
    

2、相对导入：仅限于包内使用
    （1）. :代表当前文件夹
    （2）..:代表上一层文件夹

    # 执行文件
        import practice_file.package_m as f      # import __init__.py
        f.func1()
        f.func2()
        f.func3()
        f.func4()
    
    # __init.py__文件
        from .mm1 import func1
        from .mm2 import func2
        from .mm3 import func3
        from .son_m.mm4 import func4,func5     
             
                 
"""
import practice_file.package_m as f  # import __init__.py

f.func1()
f.func2()
f.func3()
f.func4()
f.func5()