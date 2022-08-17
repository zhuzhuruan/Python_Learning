# --------------------------------------- 异常 ------------------------------------------------
# 捕捉异常可以使用try/except语句: try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
# 如果你不想在异常发生时结束你的程序，只需在try里捕获它。
# try:
# <语句>        #运行别的代码
# except <名字>：
# <语句>        #如果在try部份引发了'name'异常
# except <名字>，<数据>:
# <语句>        #如果引发了'name'异常，获得附加的数据
# else:
# <语句>        #如果没有异常发生

# try语句的工作原理如下：
# 首先，执行 try 子句 （try 和 except 关键字之间的（多行）语句）。
# 如果没有异常发生，则跳过 except 子句 并完成 try 语句的执行。
# 如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。 然后，如果异常的类型和 except 关键字后面的异常匹配，则执行 except 子句，然后继续执行 try 语句之后的代码。
# 如果发生的异常和 except 子句中指定的异常不匹配，则将其传递到外部的 try 语句中；如果没有找到处理程序，则它是一个 未处理异常，执行将停止并显示如上所示的消息。
# 一个 try 语句可能有多个 except 子句，以指定不同异常的处理程序。 最多会执行一个处理程序。 处理程序只处理相应的 try 子句中发生的异常，而不处理同一 try 语句内其他处理程序中的异常。 一个 except 子句可以将多个异常命名为带括号的元组

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except (RuntimeError, TypeError, NameError):
        pass

workfiles = 'D:/mydata/cyy/CYY_Projects/foo.txt'
try:
    with open(workfiles, "w", encoding='utf-8') as f:
        f.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
finally:  # try-finally 语句无论是否发生异常都将执行最后的代码
    print("Error: 没有找到文件或读取文件失败")
    f.closed()

try:
    fh = open(workfiles, "w", encoding='utf-8')
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print("关闭文件")
        fh.close()
except IOError:
    print("Error: 没有找到文件或读取文件失败")

# --------------------------------------- 抛出异常 ------------------------------------------------
# raise: 语句允许程序员强制发生指定的异常
