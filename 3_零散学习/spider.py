import requests
import re
import time

base_url = 'https://www.anjuke.com/shanghai/cm/p{}/'
result = []
for i in range(1,2):
    try:
        print(i)
        time.sleep(10)
        html = requests.get(base_url.format(7), 'utf-8')
        html.encoding='gbk'
        print(html)
        re_base = '(?<=(?:<em><a href="https://www.anjuke.com/shanghai/cm595176/" target="_blank">)).*(?=<(?:</a></em>))'
        child = re.findall(re_base, html.text, flags=0)
        result.append(child)
    except:
        print('error')
        pass

print(result)



