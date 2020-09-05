#！/usr/bin/python
# -*- coding: utf-8 -*-

"""
时间的表示形式
1、时间戳
以整型或浮点型表示时间的一个以秒为单位的时间间隔。
2、元组
一种python的数据结构表示，这个元组有9个整型内容
year,month,day,hours,minutes,seconds,weekday,julia day,flag(1 或 -1、0)
3、格式化字符串

"""
import time

c = time.time()
print(c)

t= time.gmtime(c)
print(t)    #UTC时间元组

#将时间戳专为本地时间元组
b = time.localtime(c)
print(b)

#将本地时间元组转成时间戳
m = time.mktime(b)
print(m)

#将时间元组转成字符串
s = time.asctime(b)
print(s)

#将时间戳转成字符串
p = time.ctime(c)
print(p)

#将时间元组转换成给定格式的字符串，参数2为时间元组，如果没有参数2，默认转成当前时间
q = time.strftime("%Y-%m-%d %H:%M:%S",b)
print(q)
print(type(q))


