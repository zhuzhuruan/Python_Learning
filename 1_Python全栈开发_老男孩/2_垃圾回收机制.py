# -*- coding:utf-8 -*-
""""""
"""
-------------------------------------------------垃圾回收机制-------------------------------------------------
一、定义
1、垃圾回收机制：简称GC，是python解释器自带的一种机制，专门用来回收不可用的变量值所占用的内存空间
             GC模块主要运用了“引用计数”（reference counting）来跟踪和回收垃圾。在引用计数的基础上，还可以通过“标记-清除”（mark and sweep）
             解决容器对象可能产生的循环引用的问题，并且通过“分代回收”（generation collection）以空间换取时间的方式来进一步提高垃圾回收的效率。

二、垃圾回收机制原理分析
1、引用计数
(1)定义：变量值被关联的次数
(2)循环引用带来的内存泄漏
    l1 = [111]
    l2 = [222]
    l1.append(l2)
    l2.append(l1)
    del l1          # 解除l1中的直接引用，但是对l2的间接引用关系并未解除
    del l2          # 解除l2中的直接引用，但是对l1的间接引用关系并未解除

2、标记-清除
(1)定义：容器对象（比如：list、set、dict、class、instance）都可以包含对其他对象的引用，所以都可能产生循环引用，而“标记-清除”就是为了解决循环引
        用的问题。
(2)变量的存储：关于变量的存储，内存中有两块区域：堆区与栈区，在定义变量时，变量名与值内存地址的关联关系存放于栈区，变量值存放于堆区，内存管理回收的
             则是堆区的内容。
(3)作用：标记-清除算法的做法是当应用程序可用的内存空间被耗尽的时，就会停止整个程序，然后进行两项工作，第一项则是标记，第二项则是清除
        -- 标记：通俗地讲就是栈区相当于“根”，凡是从根出发可以访达（直接或间接引用）的，都称之为“有根之人”，有根之人当活，无根之人当死。
                具体地：标记的过程其实就是，遍历所有的GC Roots对象(栈区中的所有内容或者线程都可以作为GC Roots对象），然后将所有GC Roots的对
                象可以直接或间接访问到的对象标记为存活的对象，其余的均为非存活对象，应该被清除。
        -- 清除：清除的过程将遍历堆中所有的对象，将没有标记的对象全部清除掉。
(4)缺点：基于引用计数的回收机制，每次回收内存，都需要把所有对象的引用计数都遍历一遍，这是非常消耗时间的，于是引入了分代回收来提高回收效率，分代回收采
        用的是用“空间换时间”的策略。

3、分代回收
(1)核心思想：在历经多次扫描的情况下，都没有被回收的变量，gc机制就会认为，该变量是常用变量，gc对其扫描的频率会降低，具体实现原理如下：
           -- 分代指的是根据存活时间来为变量划分不同等级（也就是不同的代）
              新定义的变量，放到新生代这个等级中，假设每隔1分钟扫描新生代一次，如果发现变量依然被引用，那么该对象的权重（权重本质就是个整数）加一，
              当变量的权重大于某个设定得值（假设为3），会将它移动到更高一级的青春代，青春代的gc扫描的频率低于新生代（扫描时间间隔更长），假设5分钟
              扫描青春代一次，这样每次gc需要扫描的变量的总个数就变少了，节省了扫描的总时间，接下来，青春代中的对象，也会以同样的方式被移动到老年代中。
              也就是等级（代）越高，被垃圾回收机制扫描的频率越低
           -- 回收：回收依然是使用引用计数作为回收的依据

-------------------------------------------------列表在内存的存储方式-------------------------------------------------

                                  0：值“a"的内存地址 -------------→ ”a"的内存空间
l1 = ['a', 'b', 'c] ------------→ 1：值“b"的内存地址 -------------→ ”b"的内存空间
                                  2：值“c“的内存地址 -------------→ ”c"的内存空间

l2 = l1
l1[1] = 'bbb'
print(l1)
print(l2)

"""
