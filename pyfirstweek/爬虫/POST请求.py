#！/usr/bin/python
# -*- coding: utf-8 -*-
'''
特点：把参数进行打包，单独传输

优点：数据量大，安全（当对服务器数据进行修改时建议使用post）

缺点：速度慢

'''

import urllib.request
import urllib.parse

url = "https://qzone.qq.com/"
#将要发送的数据合成一个字典，字典的键去网址里找，一般为input标签的name属性的值
data = {"name":"u","name":"p"}
#对要发送的数据进行打包
postData = urllib.parse.urlencode(data).encode("utf-8")
#请求体
req = urllib.request.Request(url,postData)
#req.add_header()
#请求
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
#print(response.data().decode("utf-8"))