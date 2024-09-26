# -*- coding: utf-8 -*-
# @Time : 2024/8/2714:51
# @Author : cyy
# @File : 随机生成bitmap.py
# @desc :


import bitarray
import random
import numpy as np
import pandas as pd


def generate_bitmap(num_bits):
    # 创建一个空的bitarray
    bitmap = bitarray.bitarray(endian='little')

    # 随机生成num_bits个比特
    for _ in range(num_bits):
        bitmap.append(random.getrandbits(1))

    return bitmap


def generate_bitmap2():
    # 创建一个初始为0的bitarray，长度为2亿
    ba = bitarray.bitarray(1000)

    # 随机设置一些位为1，模拟数据的存在
    # 例如，设置1亿个随机位为1
    for _ in range(100000000):
        ba[random.randint(0, 200000000 - 1)] = 1

    # 保存bitarray到文件
    with open('bitmap.data', 'wb') as f:
        ba.tofile(f)


def generate_bitmap3():
    # 计算需要的位数和数组的大小（以字节为单位）
    max_bits = 2e9  # 20亿位
    bits_per_byte = 8  # 每个字节包含8位
    bytes_needed = (max_bits + bits_per_byte - 1) // bits_per_byte  # 向上取整计算需要的字节数
    # 创建一个全0的字节数组来存储位图
    bitmap = np.zeros(int(bytes_needed), dtype=np.uint8)
    return bitmap


# 现在你可以使用位操作来设置或清除特定的位，例如：
# 设置第n位为1 (注意：位置是从0开始的，并且需要转换为字节和位索引)
def set_bit(bitmap, n):
    byte_index = n // 8  # 计算字节索引  整除
    bit_index = n % 8  # 计算位索引  取模
    bitmap[byte_index] |= (1 << bit_index)  # 设置特定的位为1
    return bitmap


# 清除第n位 (同样需要注意索引的计算)
def clear_bit(bitmap, n):
    byte_index = n // 8
    bit_index = n % 8
    # bitmap[byte_index] &= \~(1 << bit_index)  # 清除特定的位为0


# 检查第n位是否被设置
def is_set(bitmap, n):
    byte_index = n // 8
    bit_index = n % 8
    return (bitmap[byte_index] & (1 << bit_index)) != 0  # 检查特定的位是否被设置


def bitarray_to_bytes(bitarray_obj):
    # 确保位数是8的倍数
    bitarray_obj.append(bitarray.bitarray('0' * (8 - len(bitarray_obj) % 8)))
    return bitarray_obj.tobytes()


if __name__ == '__main__':
    # 生成一个包含1000个比特的bitmap
    bitmap = generate_bitmap(1000)
    print(bitmap)

    # bitmap = generate_bitmap3()
    # bitmap = set_bit(bitmap, 16)
    # print(bitmap)
    # with open(r'../file/bitmap.bin', 'wb') as f:
    #     f.write(bitmap.tobytes())

    # x = bitmap.tobytes()
    # print(x)

    import pickle

    # 假设我们的bitmap是一个简单的列表示例
    bitmap = [1, 0, 1, 1, 0]
    # 使用pickle序列化bitmap
    binary_data = pickle.dumps(bitmap)
    # 打印序列化后的二进制数据
    print(binary_data)
    # 反序列化回bitmap
    new_bitmap = pickle.loads(binary_data)
    # 打印反序列化后的结果
    print(new_bitmap)
