# 查找列表中两个元素之和等于某值的两个元素
def sum_num_off():
    list_a = [3, 3]
    target = 6
    dic = {}
    for i, j in enumerate(list_a):
        x = dic.get(target - j, -1)
        if x != -1:
            print(i, j)
            print(dic[target - j], target - j)
        else:
            dic[j] = i
            print(dic)


# 一组数字排列的多种情况
def sort_num_list(num_list, mode):
    if mode == 1:
        # itertools模块中的permutations方法
        import itertools
        return list(itertools.permutations(num_list, 3))
    elif mode == 2:
        # 采用循环读取去重的方式
        res = []
        for i in num_list:
            for j in num_list:
                for k in num_list:
                    if len(set((i, j, k))) == 3:
                        res.append(list((i, j, k)))
        return res


if __name__ == '__main__':
    sum_num_off()
    # print(sort_num_list([1, 2, 3, 4], 1))
