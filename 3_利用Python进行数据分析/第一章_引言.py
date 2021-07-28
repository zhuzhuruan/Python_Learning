# -*— coding:utf-8 -*-
import json

file_path = '源文件数据/1_引言/bitly_usagov.txt'
with open(file_path, 'rt', encoding='utf-8') as f:
    records = [json.loads(line) for line in f]  # 列表推导式
print(records[0], type(records))
