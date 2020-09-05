#！/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import ssl
import json

def ajaxxCrawler(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"
    }
    req = urllib.request.Request(url,headers=headers)

#使用ssl创建未验证的上下文
    context = ssl._creat_unverified_context()
    response = urllib.request.urlopen(req,context=context)

    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)

    return jsonData

'''
url = "https://movie.douban.com/subject/26213252/?from=showing"
info = ajaxxCrawler(url)
print(info)
'''
for i in (1,11):
    url = "https://movie.douban.com/subject/26213252/?from=showing"
    info = ajaxxCrawler(url)
    print(len(info))