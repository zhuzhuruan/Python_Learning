# -*- coding: utf-8 -*-
# @Time : 2022/7/2711:00
# @Author : cyy
# @File : practise.py
# @desc :


from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup
import time
import random
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import time
import random
import re

articalUrl = "/wiki/%E5%87%AF%E6%96%87%C2%B7%E8%B4%9D%E8%82%AF"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}


pages = set()
def getlinks(articalUrl):
    global pages
    url = "https://zh.wikipedia.ahau.cf" + articalUrl
    req = request.Request(url, headers=headers)
    html = urlopen(req)
    bs0bj = BeautifulSoup(html)
    try:
        print(bs0bj.find("h1").get_text())
        print(bs0bj.find(id="mw-content-text").findAll("p")[0])
        print(bs0bj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError as e:
        print("页面缺少一些属性，不过不用担心！")
    for link in bs0bj.findAll("a", href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                newpage = link.attrs["href"]
                print(newpage)
                pages.add(newpage)
                getlinks(newpage)


if __name__ == '__main__':
    # random.seed(time.time())
    # links = getlinks(articalUrl)
    # while len(links) > 0:
    #     newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    #     print(newArticle)
    #     links = getlinks(newArticle)
    getlinks(articalUrl)
