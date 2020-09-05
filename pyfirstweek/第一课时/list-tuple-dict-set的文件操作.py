#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

import pickle   #数据持久性模块

myList = [1,2,3,4,5,'sunck is a good man']
# mytuple = (1,2,3,4,5,'sunck is a good man')
path = r'C:\Users\Administrator\Desktop\python学习文档111.txt'
f = open(path, 'wb')

pickle.dump(myList, f)

f.close()

#读取
f1 = open(path, 'rb')
tempList = pickle.load(f1)
print(tempList)
f1.close()