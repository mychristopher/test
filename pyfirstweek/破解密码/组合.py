#！/usr/bin/python
# -*- coding: utf-8 -*-
import itertools

mylist = list(itertools.combinations([1,2,3,4],3))
print(mylist)
print(len(mylist))

#组合公式：m!/(n!x(m-n))