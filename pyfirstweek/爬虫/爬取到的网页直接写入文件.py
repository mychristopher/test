#！/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request

urllib.request.urlretrieve("http://www.baidu.com",filename=r"C:\Users\Administrator\Desktop\Python代码练习\爬虫\file\file2.html")

#urlretrieve在执行的过程当中，会形成一些缓存
#清除缓存
urllib.request.urlcleanup()

