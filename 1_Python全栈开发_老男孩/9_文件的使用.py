# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------文件-------------------------------------------------
一、文件的概念
1、什么是文件？
    文件是操作系统提供给用户/应用程序操作硬盘的一种虚拟的概念/接口

2、为什么要用文件？
    用户/应用程序可以通过文件将数据永久保存在硬盘中，即操作文件就是操作硬盘
    用户/应用程序直接操作的是文件，对文件进行的所有操作都是在向操作系统发送系统调用，然后再由操作系统将其转换成具体的硬盘操作

3、如何用文件？open()
    控制文件读写内容的模式：t 和 b
        强调：t和b不能单独使用，必须和r/w/a连用

    t文本（默认的模式）
        （1）读写都以str(unicode)为单位
        （2）针对的是文本文件
        （3）必须指定encoding参数

    b二进制/bytes
        （1）读写都是以bytes为单位
        （2）针对的是所有文件
        （3）一定不能指定字符编码

                with open('practice_file\\文件的使用.txt', 'rb') as f:
                    res = f.read()         # utf-8对应的二进制
                    print(res)
                    print(res.decode())    # 将utf-8对应的二进制解码为unicode对应的字符

                with open('practice_file\\pywcloud.png', 'rb') as f:
                    res = f.read()
                    print(res)

                with open('file', 'wb') as f:
                    f.write('Hello World!'.encoding('utf-8'))       # 将字符编码为utf-8模式
                    f.write('Hello World!'.encoding('gbk'))       # 将字符编码为gbk模式

    总结：b模式比t模式更通用
        （1）在操作纯文本文件方面，t模式省去了编码解码的环节，b模式则需要手动编码和解码，所以此时t模式更方便
        （2）针对非文本文件（视频、音频、图片等）只能使用b模式


二、文件操作的基本流程
1、打开文件
    （1）open(): 打开文件后需要通过close()来关闭文件
    （2）with open(): 上下文管理，打开文件后会自动关闭文件
            with open('file', 'rt', encoding='') as f:
                f.read()      # t模式会将f.read()读出的结果按照encoding=''指定的编码方式解码为Unicode

2、操作文件read()
3、关闭文件close()


三、文件读写模式
1、r模式（默认的操作模式）：只读模式
    （1）当文件不存在时报错
    （2）当文件存在时，文件指针跳到最开始的位置
            with open('file', 'rt', encoding='utf-8') as f:
                    f.read()        # 将文件内容一次性读入内存

2.w模式：只写模式
    （1)当文件不存在时，创建空文件
    （2）当文件存在时，清空文件内容，指针跳到最开始的位置
            with open('file', 'wt', encoding='utf-8') as f
                f.write('Hello World!')

    （3）以w模式打开文件并且没有关闭的情况下，连续的让文件中写入内容
            with open(file, 'wt', encoding='utf-8') as f:
                f.write('Hello World!')
                f.write('HelloHello World!')
                f.write('HelloHelloHello World!')

    （3）如果重新以w模式打开文件，则会清空文件内容，重新写入
            with open(file, 'wt', encoding='utf-8') as f:
                f.write('Hello World!')
            with open(file, 'wt', encoding='utf-8') as f:
                f.write('HelloHello World!')
            with open(file, 'wt', encoding='utf-8') as f:
                f.write('HelloHelloHello World!')

3、a模式：只追加写
        （1）在文件不存在时，创建空文件
        （2）在文件存在时，文件指针会自动跳到末尾
                with open(file, 'at', encoding='utf-8') as f:
                    f.write('Hello World!')
                    f.write('HelloHello World!')
                    f.write('HelloHelloHello World!')

    w模式与a模式的异同点：
        （1）相同点：在打开的文件不关闭的情况下，连续的写入，新写入的内容会跟在前面已经写入内容的后面
        （2）不同点：以a模式重新打开文件，不会清空文件内容，会将文件指针移到文件末尾，在文件末尾追加写入

4、+模式：可读可写，不能单独使用，必须配合r、w、a
        （1）和r、w、a配合使用时，依赖于r、w、a的特性
            <1>搭配r
                with open(file, 'rt+', encoding='utf-8') as f:
                    # 情况1：文件不存在时，直接报错
                    f.write('\n麻子:245')
                    # 情况2：文件存在时，不读文件，直接写入，指针位于文件的开头，写入的字符会覆盖原本位置的字符
                    f.write('\n麻子:245')
                    # 情况3：文件存在时，先读文件，再写入，此时文件指针位于文件的末尾，在末尾写入
                    f.read()
                    f.write('\n麻子:245')
            <2>搭配w
                with open(file, 'wt+', encoding='utf-8') as f:
                    # 情况1：文件不存在时，创建文件
                    print(f.read())
                    f.write('麻子:245')
                    # 情况2：文件存在时，会先清空文件，这时候读取文件内容为空，再写入文件，再次读取文件，此时指针已经在文件的末尾，读取仍为空
                    print(f.read())
                    f.write('麻子:245')
                    print(f.read())
            <3>搭配a
                with open(file, 'at+', encoding='utf-8') as f:
                    # 情况1：文件不存在时，创建文件
                    print(f.read())
                    f.write('麻子:245')
                    # 情况2：文件存在时，指针在文件的末尾，读取为空，写入则从末尾开始写
                    print(f.read())
                    f.write('麻子:245')
                    print(f.read())

5、x模式：只写模式
    （1）文件存在时，报错
    （2）文件不存在时，创建空文件


四、文件的循环读写
1、循环读：
    （1）readline(size=-1): 读入一行内容，如果给出参数，读入该行前size长度
            with open('practice_file\\文件的使用.txt', 'rt', encoding='utf-8') as f:
                while True:
                    res = f.readline()
                    if len(res) == 0:
                        break
                    else:
                        print(res)

    （2） <f>.readlines(hint=-1): 读入文件所有行，以每行为元素形成列表，如果给出参数，读入前hint行
            with open('practice_file\\文件的使用.txt', 'rt', encoding='utf-8') as f:
                res = f.readlines()
                print(res)

2、循环写
    （1）writelines(lines): 将一个元素全为字符串的列表写入文件（直接拼接不换行）
            with open('practice_file\\文件的使用.txt', 'wt', encoding='utf-8') as f:
                res = ['aaa', 'bbb', 'ccc']
                f.writelines()


五、文件指针的移动
1、指针移动的单位都是以字节(bytes)为单位，只有一种情况特殊：t模式下的read(n),n代表的是字符个数

2、f.seek(n, offset)
    (1)n: 指针移动的字节的个数
    (2)offset: 只有0可以在t模式下使用，1和2只能在b模式下使用，移动的单位都是字节
        -- 0:参照物是文件开头位置
        -- 1:参照物是文件当前位置
        -- 2:参照物是文件末尾位置（应该倒着移动）

3、f.tell():告知文件当前指针位置
        with open('practice_file\\文件的使用.txt', 'a+t', encoding='utf-8') as f:
            f.write('')


"""

# -------------------------------------------------案例完善-------------------------------------------------
count = 0
while count < 3:
    info_username = input("请输入您的用户名：")
    info_password = input("请输入您的密码：")
    with open('practice_file/文件的使用.txt', 'rt', encoding='utf-8') as f:
        for line in f:
            username, password = line.strip().split(':')
            if info_username == username and info_password == password:
                print("登录成功")
                while True:
                    cmd = input("请根据提示输入您的指令：1-存款 ; 2-取款 ; 3-汇款 ; q:退出 : ")
                    if cmd == 'q':
                        exit(0)
                    else:
                        print("命令{x}正在运行".format(x=cmd))
            break
        else:
            print("用户名或密码错误")
            count += 1
else:
    print("输入错误超过3次，程序退出")

# -------------------------------------------------文本文件的copy案例-------------------------------------------------
src_file = input("请输入源文件路径:").strip()
dst_file = input("请输入目标文件路径:").strip()
with open(r'{}'.format(src_file), 'rt', encoding='utf-8') as f:
    with open(r'{}'.format(dst_file), 'wt', encoding='utf-8') as w:
        res = f.read()
        w.write(res)

with open(r'{}'.format(src_file), 'rb') as f:
    with open(r'{}'.format(dst_file), 'wb') as w:
        res = f.read()
        w.write(res)

# -------------------------------------------------模仿监测日志-------------------------------------------------
import time

with open('practice_file\\文件的使用.txt', 'a+t', encoding='utf-8') as f:
    f.write('赵一:524')

with open('practice_file\\文件的使用.txt', 'rb') as f:
    f.seek(0, 2)  # 指针移动到文件末尾
    while True:
        line = f.readline()
        if len(line) == 0:
            time.sleep(0.5)
        else:
            print(line.decode('utf-8'))
