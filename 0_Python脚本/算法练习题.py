# 查找列表中两个元素之和等于某一值的两个元素
list_a = [3, 3]
target = 6
dic = {}
for i, j in enumerate(list_a):
    x = dic.get(target-j, -1)
    if x != -1:
        print(i, j)
        print(dic[target-j], target-j)
    else:
        dic[j] = i
        # print(dic)