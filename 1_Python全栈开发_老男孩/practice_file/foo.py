# -*- coding:utf-8 -*-
print('模块文件foo.by'.center(100,'='))
# 文件名：foo.py
print(__name__)

x=222
def get():
    print(x)

def change():
    global x
    x=0

class Foo:
    def func(self):
       print('from the func')


# 调用
if __name__ == '__main__':
    get()
    change()


