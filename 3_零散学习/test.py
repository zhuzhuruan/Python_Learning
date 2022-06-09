from Practice import fibo

if __name__ == '__main__':
    print('I am a import test')

# 导入模块
from Practice import fibo
if __name__ == '__main__':
    fibo.make_pizza(16, 'pepperoni')
    fibo.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入特定函数
from Practice import fibo
if __name__ == '__main__':
    fibo.make_pizza(16, 'pepperoni')
    fibo.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


