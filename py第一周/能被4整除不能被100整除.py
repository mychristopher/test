#！/usr/bin/python
# -*- coding: utf-8 -*-
#能被4整除但是不能被100整除  或者   能被400整除

year = int(input())
if year % 400 ==0 or (year % 4 == 0 and year % 100 !=0):
    print("是闰年")
else:
    print("不是闰年")