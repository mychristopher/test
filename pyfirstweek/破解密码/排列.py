#！/usr/bin/python
# -*- coding: utf-8 -*-
import itertools

mylist = list(itertools.permutations([1,2,3,4],3))
print(mylist)
print(len(mylist))

#排列的可能性次数：n!/(n-m)!