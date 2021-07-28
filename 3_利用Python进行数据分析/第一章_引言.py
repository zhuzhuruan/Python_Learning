# -*— coding:utf-8 -*-
import json

file_path = '源文件数据/1_引言/bitly_usagov.txt'
with open(file_path, 'rt', encoding='utf-8') as f:
    records = [json.loads(line) for line in f]  # 列表推导式

tz_dic = {}
for item in records:
    if 'tz' in list(item.keys()):
        tz_dic[item['tz']] = tz_dic.get(item['tz'], 0) + 1
item = list(tz_dic.items())
item.sort(key=lambda x: x[1], reverse=True)
print(item)

