#！/usr/bin/python
# -*- coding: utf-8 -*-
#计算1+2+3+......+100
sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print("sum = %d" %(sum))

str = "sunck is a handsome man"
index = 0
while index < len(str):
    print("str[%d] = %s" % (index, str[index]))
    index += 1