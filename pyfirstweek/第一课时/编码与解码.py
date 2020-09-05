#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

#编码
path = r'C:\Users\Administrator\Desktop\python学习文档111.txt'
with open(path, 'wb') as f1:
    str = 'sunck is a good man凯'
    f1.write(str.encode('utf-8'))
#解码
with open(path, 'wb') as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newData = data.decode('utf-8')
