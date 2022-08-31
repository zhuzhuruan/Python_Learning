# -*- coding: utf-8 -*-
# @Time : 2022/8/1616:02
# @Author : cyy
# @File : 爬取网页标题.py
# @desc :

import string
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import time
import random
import re
from urllib import request
import pandas as pd

User_Agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    # "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
    # "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    # "Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
    # "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
    # "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"

]


def read_data(path, sheet_name):
    data = pd.read_excel(path, sheet_name=sheet_name)
    return data


def get_links(url):
    random_agent = User_Agents[random.randint(0, len(User_Agents) - 1)]
    headers = {"User-Agent": random_agent,
               "Agent": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
               }
    # 将中文字符转换
    url = urllib.parse.quote(url, safe=string.printable)
    req = request.Request(url, headers=headers)
    try:
        time.sleep(random.randint(5, 15))
        html = urlopen(req)
    except HTTPError as e:
        return None
    try:
        bs0bj = BeautifulSoup(html)
        # print(bs0bj)
        # 标题储存在h3标签下
        title_list = []
        for link in bs0bj.findAll("h3"):
            title = link.find("a").get_text()
            if "href" in link.find("a").attrs:
                href = link.find("a").attrs["href"]
            else:
                href = None
            _dict = {"title": title, "href": href}
            if re.search('公司|企业|集团', title):
                title_list.append(_dict)
        return title_list
    except AttributeError as e:
        return None


def clean_data(data):
    # print(data)
    if re.search('[\u4e00-\u9fa5]|[a-zA-Z]', data) and len(re.sub('[0-9]|[(（）),，.?]|[—_-]5[Gg]', '', data)) > 2:
        data_split = re.split("[-_—]|[ %:!！@#\$\^&\*()（），,<>\.\+\?\|]", re.sub("[—_-](?:5|2.4)[Gg]", "", data))
        data_clean = [i for i in data_split if re.search('[\u4e00-\u9fa5]', data) or re.search('[a-zA-Z]', i)]
        if not data_clean:
            return None
        else:
            data_clean.sort(key=lambda x: len(x), reverse=True)
            return data_clean[0]
    else:
        return None


def get_data_url(data):
    data["ssid_clean"] = data["ssid"].apply(lambda x: clean_data(x))
    data["url"] = None
    data["title"] = None
    for i in data.index:
        print(i, data.loc[i, "ssid_clean"])
        if i > 600:
            if data.loc[i, "ssid_clean"] is not None:
                data.loc[i, "url"] = "https://www.baidu.com/s?wd=" + data.loc[i, "ssid_clean"]
                title_list = get_links(data.loc[i, "url"])  # data.loc[i, "url"]
                if title_list:
                    data.loc[i, "title"] = str([i.get("title") for i in title_list])
                    print(i, data.loc[i, "title"], data.loc[i, "ssid_clean"])
    data.to_excel(r'C:\Users\caoyuanyuan\Desktop\项目文档\2-企业WiFi库\不同行业wifi分拣\test结果1.xlsx')


if __name__ == '__main__':
    path = r"C:\Users\caoyuanyuan\Desktop\项目文档\2-企业WiFi库\不同行业wifi分拣\test.xlsx"
    data = read_data(path, sheet_name="Sheet1")
    # print(data.head(100))
    get_data_url(data)

    # 单个测试
    # res = get_links("https://www.baidu.com/s?wd=Thaiwoo")
    # print(res)

    # res = re.sub('[0-9]|[(（）),，.?]|[—_-]5[Gg]', '', '1104A')
    # print(res)
