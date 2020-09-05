#！/usr/bin/python
# -*- coding: utf-8 -*-
import itertools

mylist = list(itertools.product([0,1,2,3,4,5,6,7,8,9,],
                                repeat=5))
#print(mylist)
print(len(mylist))

