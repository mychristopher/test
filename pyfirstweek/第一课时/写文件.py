#！/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cyf'

import time

path = r'C:\Users\Administrator\Desktop\python学习文档111.txt'
f = open(path, 'w')

'''
#写文件
f.write('sunck is a good man')   #将信息写入缓存区
f.flush()    #刷新缓存区，直接把内部缓存区的数据立刻写入文件，而不是被动的等待、自动刷新缓存区写入#加\n也会自动刷新缓存区
while 1:
    f.write('sunck is a good man')
    time.sleep(0.001)   #缓存区满了的话会自动写入缓存区

f.close()
'''

with open(path, 'a') as f2:
    f2.write('good man')