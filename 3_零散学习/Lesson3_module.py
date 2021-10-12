# 如果你从Python解释器退出并再次进入，之前的定义（函数和变量）都会丢失
# Python有一种方法可以把定义放在一个文件里，并在脚本或解释器的交互式实例中使用它们。这样的文件被称作 模块 ；模块中的定义可以 导入 到其它模块或者 主 模块
# 模块是一个包含Python定义和语句的文件。文件名就是模块名后跟文件后缀 .py
# 在一个模块内部，模块名（作为一个字符串）可以通过全局变量 __name__ 的值获得

# fibo 模块: 建立为一个python脚本
# Fibonacci numbers module
def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# 调用模块
from Practice import fibo  # 注意路径

fibo.fib(1000)
fibo.__name__

# --------------------------------------- __name__ ------------------------------------------------
if __name__ == '__main__':
    print()

# 1：__name__是一个变量。前后加了双下划线是因为是因为这是系统定义的名字。普通变量不要使用此方式命名变量。
# 2：Python有很多模块，而这些模块是可以独立运行的！这点不像C++和C的头文件。
# 3：import的时候是要执行所import的模块的。
# 4：__name__就是标识模块的名字的一个系统变量。这里分两种情况：
# 假如当前模块是主模块（也就是调用其他模块的模块），那么此模块名字就是__main__，通过if判断这样就可以执行“__main__:”后面的主函数内容；
# 假如此模块是被import的，则此模块名字为文件名字（不加后面的.py），通过if判断这样就会跳过“__mian__:”后面的内容。
# 通过上面方式，python就可以分清楚哪些是主函数，进入主函数执行；并且可以调用其他模块的各个函数等等。
# 1. 如果模块是被导入，__name__的值为模块名字
# 2. 如果模块是被直接执行，__name__的值为’__main__’

# 实例: fibo.py & 清洗脚本.py

# 内置函数 dir() 用于查找模块定义的名称。 它返回一个排序过的字符串列表
dir(fibo)